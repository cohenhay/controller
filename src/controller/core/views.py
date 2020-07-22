from django.db.models import Q
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView , ListView
from tablib import Dataset
from .filter import CoreFilter
from .models import Server
from .resources import ServerResource



def search(request):
    servers_list = Server.objects.all()
    server_filter = CoreFilter(request.GET, queryset=servers_list)
    return render(request, 'home.html', {'filter': server_filter})


def upload(request):
    file_format = request.POST['file-format']
    server_resource = ServerResource()
    dataset = Dataset()
    new_servers = request.FILES['importData']
    imported_data = dataset.load(new_servers.read().decode('utf-8'),format='xlsx')
    result = server_resource.import_data(dataset, dry_run=True)                                                                 
    server_resource.import_data(dataset, dry_run=False) 
    return render(request, 'home.html')


