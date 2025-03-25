from django.shortcuts import render,HttpResponse,redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

from django.contrib import messages
# Create your views here.

def gmails(request):
    return render(request,'gmails/index.html')

def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        template = render_to_string('email-template.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        })

        emailSender = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            # ACA VA EL CORREO O LA LISTA DE CORREOS A LOS QUE QUIERO ENVIAR ESTE EMAIL. PUEDE SER UNO O TANTOS COMO LOS QUE DESEE
            # SI ES UNO SOLO, COLOCO EL CORREO UNICO ENTRE COMILLAS SIMPLES Y NADA MAS. SI AGREGO MÁS TENGO QUE SEPARARLOS CON UNA COMA ','
            ['correo1@correo.com','correo2@correo.com']
        )
        emailSender.content_subtype = 'html'
        emailSender.fail_silently = False
        emailSender.send()

        messages.success(request, 'El correo electrónico se envió correctamente')
        return redirect('/gmails/')

