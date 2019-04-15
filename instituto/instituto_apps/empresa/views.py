from django.shortcuts import render,redirect
from empresas.models import Representante,Empresa
from main.models import Persona
from datetime import date, datetime
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from instituto.settings import DEFAULT_FROM_EMAIL
from django.contrib import messages

from django.core.mail import EmailMessage

@login_required(login_url='login')
def ListarEmpresa(request):

    datos = Representante.objects.filter(persona__tipo_persona = 'R', persona__usuario__is_superuser = False)
    return render(request, 'empresa/empresas.html', {'datos': datos})

@login_required(login_url='login')
def CambiarEstado(request,id):

    if request.method == 'POST':
        print(request.POST)
        if request.is_ajax():
            representante = Representante.objects.get(id=id)
            empresa = Empresa.objects.get(id=representante.empresa.id)
            persona = Persona.objects.get(id=representante.persona.id)
            print(representante)
            if representante.estado == 'A':
                representante.estado = 'I'
                persona.enviar_correo = False
                representante.save()
                persona.save()
            else:
                representante.estado = 'A'
                persona.enviar_correo = True
                representante.save()
                persona.save()
                body = render_to_string('correos/CuentaActiva.html', {'email': persona.usuario.email,
                                                                      'domain': request.META['HTTP_HOST'],
                                                                      'protocol': 'http'
                                                                      })
                email_message = EmailMessage(subject='Su cuenta ha sido activada', body=body,
                                             from_email=DEFAULT_FROM_EMAIL,
                                             to=[persona.usuario.email])
                email_message.content_subtype = 'html'
                email_message.send()


            if empresa.estado == 'A':
                empresa.estado = 'I'
            else:
                empresa.estado = 'A'

            empresa.save()

            if persona.estado == 'A':
                persona.estado = 'I'
            else:
                persona.estado = 'A'
            persona.save()


    return redirect("empresa:index")

