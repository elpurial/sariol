from django.urls import path
from .views import VRegistro,cerrar_sesion,logear
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
                 
    path('',VRegistro.as_view() , name="autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"), 
    path('logear', logear, name="logear"),   
    
    
    
    ]


