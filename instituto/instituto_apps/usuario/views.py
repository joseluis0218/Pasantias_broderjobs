
from django.shortcuts import render, redirect
from main.models import Persona
from users.models import User
from .forms import UsuarioForm,PersonaForm,UsuarioEditForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from instituto.settings import DEFAULT_FROM_EMAIL
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def ListarUsuario(request):

    personas = Persona.objects.filter(tipo_persona = 'I', usuario__is_superuser = False)
    paginator = Paginator(personas, 15) #Show 15 contacts per page
    page = request.GET.get('page')
    personas = paginator.get_page(page)

    return render(request, 'usuario/usuarios.html', {'personas' : personas})

@login_required(login_url='login')
def CrearUsuario(request):

    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        persona = Persona()
        if not request.is_ajax():
            print(request.POST)
            if usuario_form.is_valid():
                usuario = usuario_form.save()
                print(usuario.id)
                usuario.username = 'user_000' + str(usuario.id)
                usuario.password = User.objects.make_random_password()
                usuario.set_password('BroderjobsPassword19')
                usuario.save()
                persona.usuario = usuario
                persona.tipo_persona = 'I'
                persona.save()
                body = render_to_string('correos/CuentaCreada.html', {'name': usuario.first_name,
                                                                  'email': usuario.email,
                                                                  'domain': request.META['HTTP_HOST'],
                                                                   'uid': urlsafe_base64_encode(force_bytes(usuario.pk)).decode(),
                                                                  'token': default_token_generator.make_token(usuario),
                                                                  'protocol': 'http'
                                                                  })
                email_message = EmailMessage(subject='Su cuenta ha sido creada', body=body, from_email=DEFAULT_FROM_EMAIL,
                                         to=[usuario.email])
                email_message.content_subtype = 'html'
                email_message.send()
                messages.add_message(request, messages.SUCCESS, 'Usuario registrado correctamente')
                messages.add_message(request, messages.WARNING, 'Continúe el proceso de registro siguiendo el link enviado al siguiente correo : '+usuario.email)
                return redirect('usuario:index')

    else:
        usuario_form = UsuarioForm()

    return render(request,'usuario/crear-usuario.html',{'usuario_form':usuario_form})

@login_required(login_url='login')
def VerUsuario(request,id):
    persona_form = None
    usuario_form = None

    persona = Persona.objects.get(id=id)
    usuario = User.objects.get(id=persona.usuario.id)
    if request.method == 'GET':
        persona_form = PersonaForm(instance=persona)
        usuario_form = UsuarioForm(instance=usuario)
    return render(request,'usuario/ver-usuario.html',{'persona_form' : persona_form,'usuario_form': usuario_form})

@login_required(login_url='login')
def EditarUsuario(request,id):
    persona_form = None
    usuario_form = None
    persona = Persona.objects.get(id=id)
    usuario = User.objects.get(id=persona.usuario.id)

    if request.method == 'GET':
        usuario_form = UsuarioEditForm(instance=usuario)

    else:
        usuario_form = UsuarioEditForm(request.POST, instance=usuario)
        if not request.is_ajax():
            if usuario_form.is_valid():
                usuario_form.save()
                print(request.POST)
                messages.add_message(request, messages.SUCCESS, 'Usuario actualizado correctamente')
            return redirect('usuario:index')

    return render(request, 'usuario/editar-usuario.html', {'usuario_form' : usuario_form})

@login_required(login_url='login')
def EliminarUsuario(request,id):
    persona = Persona.objects.get(id=id)
    usuario = User.objects.get(id=persona.usuario.id)
    if request.method == 'POST':
        print(request.POST)
        persona.delete()
        usuario.delete()
        messages.add_message(request, messages.WARNING, 'Usuario eliminado correctamente')
        return redirect('usuario:index')

    return render(request,'usuario/eliminar-usuario.html',{'usuario': usuario})