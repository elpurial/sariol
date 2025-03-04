from django.urls import path
from .import views




urlpatterns = [
    
    path('',views.procesar_pedidos, name="procesar_pedidos"),
    
    ]