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

# class HomeView(ListView):
   


#     model = Server
#     template_name = 'home.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = CoreFilter(self.request.GET, queryset=set.get_queryset())
#         return render(request , template_name, context)

    # def get(self,request, *args, **kwargs):
    #     queryset = Server.objects.all()
    #     context = {
    #         "object_list":queryset
    #     }
    #     return render(request , "home.html" , context)
    
    
    # def get_queryset(self,request, *args, **kwargs):
    #     queryset = self.request.GET.get('q')
    #     object_list = Server.objects.filter(Q(hostname__icontains=queryset) | Q(ipadress__icontains=queryset) | Q(os__icontains=queryset))
    #     context = {
    #         "object_list":queryset
    #     }
    #     return render(request , "home.html" , context)




