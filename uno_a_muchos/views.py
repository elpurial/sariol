from django.shortcuts import render
from .models import  Casa_Rodolfo,Habitaciones
from django.http import HttpResponse
from datetime import date
from django.db.models import F, Sum


# Create your views here.
def crear(request):
    
    casa=Casa_Rodolfo(nombre="Adonis", cant_habitaciones=5)
    casa.save()    
    casa1=Casa_Rodolfo(nombre="Xiomara", cant_habitaciones=4)
    casa1.save()  
   
    #disponibilidad = Habitaciones.objects.annotate(un campo - F('ocupadas') )
    habitaciones=Habitaciones(ocupadas=7,disponibles=2,fecha=date(2025,2,8),nombre=casa)    
    habitaciones.save()
    habitaciones1=Habitaciones(ocupadas=7,disponibles=2,fecha=date(2025,2,8), nombre=casa1)    
    habitaciones1.save()
    #resultado=habitaciones.nombre
    
    #acceder desde la casa al valor relacionado de las habitaciones     
    consulta1=habitaciones.nombre.nombre
    consulta2=habitaciones1.nombre.nombre
    
    return HttpResponse(consulta1 +  "/" + consulta2  ) 