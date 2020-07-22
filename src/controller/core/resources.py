from import_export import resources
from .models import Server

class ServerResource(resources.ModelResource):
    class Meta:
        model = Server