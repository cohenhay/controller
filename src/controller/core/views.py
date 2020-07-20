from django.db.models import Q
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView , ListView
from .filter import CoreFilter
from .models import Server


def search(request):
    servers_list = Server.objects.all()
    server_filter = CoreFilter(request.GET, queryset=servers_list)
    return render(request, 'home.html', {'filter': server_filter})
