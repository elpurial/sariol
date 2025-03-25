from django.shortcuts import render,redirect
from .carro import Carro
from tienda.models import Producto



# Create your views here.
def agregar_producto(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("tienda")

    
def eliminar_producto(request,producto_id):#pasamos los parametros
    carro=Carro(request) #creamos el carro
    producto=Producto.objects.get(id=producto_id)#obtenemos el producto_id del modelo
    carro.eliminar(producto=producto)#llaman=mos al metodo eliminar de la clase Carro
    return redirect("tienda") #redireccionamos a la tienda  
    
  
def restar_producto(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("tienda")    
    
def limpiar_carro(request,producto_id):
    carro=Carro(request)   
    carro.limpiar_carro()
    return redirect("tienda")  
