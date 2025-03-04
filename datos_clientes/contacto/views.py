from django.shortcuts import render,HttpResponse,redirect
from .import views
from .forms import Form_contacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
     formulario_automatico=Form_contacto()
     if request.method=="POST":
          formulario_automatico=Form_contacto(data=request.POST) 
          if formulario_automatico.is_valid():
               nombre=request.POST.get("nombre")
               asunto=request.POST.get("asunto")
               sender=request.POST.get("sender")
             
               email=EmailMessage("Mensaje recibido",
               "El usuario con nombre{},con el correo {},envio el siguiente mensaje:\n\n{}".format(nombre,sender,asunto),
               "",["sariolje56@gmail.com"])
                         
               try: 
                                                  
                    email.send()
                    messages.success(request, 'El correo electrónico se envió correctamente')
             
                    return redirect("/contacto/?valido")
               except:
                    return redirect("/contacto/?novalido")
              
     return render(request,'contacto/contacto.html',{"miform":formulario_automatico}) 