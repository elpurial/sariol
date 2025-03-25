from django.contrib import admin
from .models  import Categorias,Post
# Register your models here.
class Categoria_admin(admin.ModelAdmin):
    readonly_fields=('created','updated')
class Post_admin(admin.ModelAdmin):
     readonly_fields=('created','updated')   
    
admin.site.register(Categorias,Categoria_admin)
admin.site.register(Post,Post_admin)
# Register your models here.
