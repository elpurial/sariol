from django.urls import path
from . import views 

urlpatterns = [
        
     path('consultas/', views.consultas, name="consultas"),
     path('actualizar/', views.actualizar, name="actualizar"),
     path('formulario/', views.formulario, name="formulario"),
     path('suceso/', views.suceso, name="suceso"),
     path('crear/', views.crear, name="crear"),
     path('guardar/', views.guardar, name="guardar"),
     
     
     ]