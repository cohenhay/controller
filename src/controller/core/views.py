from django.db.models import Q
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView , ListView
from .models import Server
class HomeView(TemplateView):
        
    def get(self,request, *args, **kwargs):
        queryset = Server.objects.all()
        context = {
            "object_list":queryset
        }
        return render(request , "home.html" , context)
        



