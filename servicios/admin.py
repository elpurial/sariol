from django.contrib import admin
from .models  import Servicios
# Register your models here.
class Fechas(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
admin.site.register(Servicios,Fechas)

