from django.contrib import admin
from .models import *

# admin personalization
admin.site.site_header = ""
admin.site.index_title = ""
admin.site.site_title = ""


# model admins
class ClientCatalogAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


# Register your models here.
admin.site.register(Automovil)
admin.site.register(Modelo)
admin.site.register(Caracteristicas)
admin.site.register(Contrato)
