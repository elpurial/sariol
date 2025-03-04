from django.contrib import admin
from .models  import Categoria_producto,Producto
# Register your models here.
class Categoria_producto_admin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
class Producto_admin(admin.ModelAdmin):
    readonly_fields=('created','updated')    
    
admin.site.register(Categoria_producto,Categoria_producto_admin)
admin.site.register(Producto,Producto_admin)

