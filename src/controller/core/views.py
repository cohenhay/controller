from django.db.models import Q
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomeView(TemplateView):
    def get(self,request, *args, **kwargs):
        context = {}
        print (request)
        print(args,kwargs,"empty")
        return render(request , "home.html" , context)
        



