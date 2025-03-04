from django.shortcuts import render,HttpResponse
from .models import Producto


# Create your views here.


def tienda(request):
    producto=Producto.objects.all()    
    return render(request,'tienda/tienda.html', {"producto":producto} )
 