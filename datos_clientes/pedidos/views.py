from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido,LineaPedidos
from carro.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


# Create your views here.
@login_required(login_url="/autenticacion/logear")
def procesar_pedidos(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedidos=list()
    for key, value in carro.carro.items():
        lineas_pedidos.append(LineaPedidos(
            
          producto_id=key,
          cantidad=value["cantidad"],
          user=request.user,
          pedido=pedido  
            
        ))
    LineaPedidos.objects.bulk_create(lineas_pedidos)
    enviar_mail(
        pedido=pedido,
        lienas_pedidos=lineas_pedidos,
        nombreusuario=request.user.username,
        #mailusuario=request.user.mail
        
      )
    messages.success(request,"El pedido se ha creado correctamente" )
    return redirect('/')

def enviar_mail(**kwargs):
    asunto="Gracias por el pedido, lo espermos en casa"
    mensaje=render_to_string("emails/pedido.html",{
      "pedido": kwargs.get("pedido"),
      "lineas_pedidos" :kwargs.get("lineas_pedidos"),
      "nombreusuario" :kwargs.get("nombreusuario"),
    })
    mensaje_texto=strip_tags(mensaje)
    from_email="sariolje56@gmail.com"
    to=kwargs.get("emailusuario" )
    
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)