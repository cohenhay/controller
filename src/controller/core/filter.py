import django_filters
from .models import Server

class CoreFilter(django_filters.FilterSet):

    class Meta:
        model = Server
        fields = {
        'hostname': ['icontains',],
        'os':       ['icontains',],
        }