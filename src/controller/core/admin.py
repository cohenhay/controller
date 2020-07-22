from django.contrib import admin
from .models import Server
from import_export.admin import ImportExportModelAdmin



# admin.site.register(Server)


@admin.register(Server)
class ServerAdmin(ImportExportModelAdmin):
    pass