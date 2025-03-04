from django.shortcuts import render

from .models import Gestor,Usuario
from django.http import HttpResponse

# Create your views here.
def crear(request):
    # Crear objetos
    gestor1 = Gestor.objects.create(nombre="Juan")
    usuario1 = Usuario.objects.create(nombre="Maria", email="maria@example.com")
    
    # Relación básica (sin campos adicionales)
    gestor1.usuarios.add(usuario1)
    
    # Obtener todos los usuarios de un gestor
    gestor1.usuarios.all()
    
    
    return HttpResponse(gestor1)