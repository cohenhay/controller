from django.db.models import Q
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView , ListView
from .filter import CoreFilter
from .models import Server
from .resources import ServerResource
from tablib import Dataset
from django.contrib import messages



def home_view(request):
    servers_list = Server.objects.all()
    server_filter = CoreFilter(request.GET, queryset=servers_list)
    if request.method == 'POST':
        server_resource = ServerResource()
        dataset = Dataset()
        new_servers = request.FILES['myfile']
        imported_data = dataset.load(new_servers.read())
        result = server_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            server_resource.import_data(dataset, dry_run=False)  # Actually import now
        #need to add user message later if file is invalid
    return render(request, 'home.html', {'filter': server_filter})

def upload_server(request):
    pass
def delete_server():
    pass

