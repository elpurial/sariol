from django.shortcuts import render,HttpResponse
from .models import Servicios

# Create your views here.


def servicios(request):
    servicios=Servicios.objects.all().order_by('-id')[:1]   
    return render(request,'servicios/servicios.html', {"servicio":servicios})

