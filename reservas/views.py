from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Reserva,Disponibilidad
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

def consultas(request):
    # Obtener todos los registros 
    # contact_list = Reserva.objects.all()
    
    #filtro por condicion
    #contact_list=Reserva.objects.filter(correo = 'ebeltran@example.net')
    
    #filtrar un unico objeto de la tabla 
    #contact_list = Reserva.objects.get(id=2)
    
    #limite de las consultas
    #contact_list = Reserva.objects.all()[:5]
    
    #rangos de registros de la tabla desde uno a otro 
    #contact_list = Reserva.objects.all()[10:5]
    
    #métodos de ordenación descendente ("-correo")
    #contact_list = Reserva.objects.all().order_by("correo","-correo")
    
    #obtenner todos los elementos cuyos id =< 15
    #contact_list = Reserva.objects.filter(id__lte =15)
    
    #obtener todos los clientes que tienen en la fila cliente la palabra magazine
    contact_list = Reserva.objects.filter(cliente__contains="magazine") 
    paginator = Paginator(contact_list, 10)  # Show 25 contacts ppor paginas.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "consultas/consulta.html", {"page_obj": page_obj})

def actualizar(request):
    cliente= Reserva.objects.get(id=1)
    cliente.cliente="José E Pérez sariol"
    cliente.correo="sariolje56@gmail.com"
    cliente.save()
    return HttpResponse("Datos actualizado")



def formulario(request):
    return render(request, "consultas/form.html", {})

def suceso(request):
    if (request.method != 'GET' ):
        return HttpResponse('El  metodo POST no esta permitido aqui')   
   
    correo= request.GET['correo']
    return render(request, "consultas/success.html", {'correo':correo})


     
def guardar(request):
   
    if request.method == "POST":
               
        cliente = request.POST['cliente']
        correo = request.POST['correo']
        cant_habitaciones = request.POST['cant_habitaciones']
        cant_dias = request.POST['cant_dias']
        pais = request.POST['pais']
        cena = request.POST['cena']
        desayuno = request.POST['desayuno']
        fecha_entrada = request.POST['fecha_entrada']
    
        fecha_salida = request.POST['fecha_salida']
        cant_personas = request.POST['cant_personas']
        comentarios = request.POST['comentarios']
               
        reserva = Reserva.objects.create(
        cliente=cliente, correo=correo,  cant_habitaciones= cant_habitaciones, cant_dias = cant_dias,
        pais=pais, cena = cena, desayuno=desayuno,fecha_entrada=fecha_entrada,fecha_salida=fecha_salida,
        cant_personas=cant_personas, comentarios=comentarios)       
        
        messages.success(request, '¡Reserva registrada!')
   
          
       
    return render(request, "consultas/post.html", {})
           
    
def crear(request):
    return render(request, "consultas/post.html", {}) 
   
    
    
    

