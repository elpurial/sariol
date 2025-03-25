from django.shortcuts import render
from .models import Casa,Propietario
from django.http import HttpResponse
# Create your views here.

def crear(request):
    #creando los elementos
    casa=Casa(nombre="Duransguesthouse",direccion="San_Esteban 615 / San_Ramón y Lugareño")
    casa2=Casa(nombre="Casa_adonis",direccion="Marti 313 / Hospital y San_Antonio")
    casa.save()
    casa2.save()
    propietario=Propietario(casa=casa, nombre="Rodolfo Duran Rodríguez", ci=56012126586,celular=53271799 )
    adonis=Propietario(casa=casa2, nombre="Adonis Duran", ci=15268947,celular=456987)
    propietario.save()
    adonis.save()
    return HttpResponse(propietario.casa.nombre)
