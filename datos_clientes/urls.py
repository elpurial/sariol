"""
URL configuration for datos_clientes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),   
    path('',include('tools.urls')),
   
    path('servicios/', include('servicios.urls')),
    path('blog/', include('blog.urls')), 
    path('contacto/', include('contacto.urls')),
    path('gmails/', include('gmails.urls')),
    path('tienda/', include('tienda.urls')), 
    path('carro/', include('carro.urls')), 
    path('autenticacion/', include('autenticacion.urls')),
    path('pedidos/', include('pedidos.urls')), 
    path('reservas/', include('reservas.urls')), 
    path('uno_a_uno/', include('uno_a_uno.urls')), 
    path('uno_a_muchos/', include('uno_a_muchos.urls')), 
                        
   
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
