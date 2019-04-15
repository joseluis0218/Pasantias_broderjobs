from django.shortcuts import render,redirect,render_to_response,HttpResponseRedirect
from django.contrib.auth import authenticate, login

from django.contrib import messages
from .models import Persona
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm
from django.contrib import messages
from .models import Persona
from .forms import UsuarioForm
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from instituto.settings import DEFAULT_FROM_EMAIL
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text
from users.models import User
from django.core.validators import validate_email
import smtplib
def LoginInstituto(request):

    form = None
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            persona = Persona()
            try:
                persona = Persona.objects.get(usuario__id=user.id)
                print(persona)
            except persona.DoesNotExist:
                persona = None
            if persona is not None:
                if persona.estado != 'I':
                    if persona.tipo_persona == 'I':
                        login(request, user)
                        return redirect('oportunidad:index')
                    elif persona.tipo_persona == 'E':
                        messages.add_message(request, messages.ERROR, "Lo sentimos, estás intentando iniciar sesión como Instituto con un usuario de tipo Estudiante.")
                        return redirect('login')
                    else:
                        messages.add_message(request, messages.ERROR, "Lo sentimos, estás intentando iniciar sesión como Instituto con un usuario de tipo Empresa.")
                        return redirect('login')
                else:
                    messages.add_message(request, messages.ERROR,
                                         "Lo sentimos, para acceder al sistema necesitar activar su cuenta a tráves del link que se le ha enviado a su correo.")
                    return redirect('login')
            else:
                messages.add_message(request, messages.ERROR,
                                     "Lo sentimos, estás intentando iniciar sesión como Instituto con un usuario de tipo Administrador.")
                return redirect('login')

        else:
            messages.add_message(request, messages.ERROR, 'Email o contraseña inválido, inténtelo de nuevo.')
            return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request,'main/login.html',{'form' : form})


def CrearUsuarioInstituto(request):

    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        persona = Persona()
        if not request.is_ajax():
            print(request.POST)
            if usuario_form.is_valid():
                try:
                    usuario = usuario_form.save()
                    usuario.username = 'user_000' + str(usuario.id)
                    usuario.save()
                    persona.usuario = usuario
                    persona.estado = 'I'
                    persona.tipo_persona = 'I'
                    persona.save()
                    new_user = authenticate(username=request.POST['email'], password=request.POST['password1'])
                except Exception:
                    messages.add_message(request,messages.ERROR,'Error en el proceso de registro, intente registrarse nuevamente')

                try:
                    body = render_to_string('correos/CuentaRegistroInstituto.html', {'nombre': usuario.first_name,
                                                                          'email': usuario.email,
                                                                          'domain': request.META['HTTP_HOST'],
                                                                          'uid': urlsafe_base64_encode(
                                                                              force_bytes(usuario.pk)).decode(),
                                                                          'token': default_token_generator.make_token(
                                                                              usuario),
                                                                          'protocol': 'http'
                                                                          })
                    email_message = EmailMessage(subject='Registro en Cetemin', body=body,
                                                 from_email=DEFAULT_FROM_EMAIL,
                                                 to=[usuario.email])
                    email_message.content_subtype = 'html'
                    email_message.send()
                except smtplib.SMTPException:
                    messages.add_message(request, messages.ERROR, 'Oops! parece que tu correo no es valido, porfavor intenta registrarte nuevamente.')

                correo = str(request.POST['email'])
                messages.add_message(request, messages.SUCCESS,
                                     "Te hemos enviado un mail a "+correo+". Ábrelo y dale click en ACTIVAR CUENTA. Para tener acceso a la aplicación")
                return redirect('login')
    else:
        usuario_form = UsuarioForm()
    return render(request,'main/instituto-registrar.html',{'usuario_form':usuario_form})


def VerificarCuenta(request,uidb64=None, token=None, token_generator=default_token_generator):

    UserModel = User()
    link_valid = False

    assert uidb64 is not None and token is not None


    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        persona = Persona.objects.get(usuario_id = user.id, estado = 'I')
    except (TypeError, ValueError,OverflowError,UserModel.DoesNotExist,Persona.DoesNotExist):
        user = None
        persona = None
        link_valid = False

    if user is not None and persona is not None and token_generator.check_token(user,token):
        link_valid = True

        persona_creada = Persona.objects.get(usuario_id=user.id)

        persona_creada.estado = 'A'

        persona_creada.save()


        login(request,user)
        return redirect('oportunidad:index')
    else:
        messages.add_message(request,messages.ERROR,"Error en el proceso de activación")
        return redirect('login')


def OlvidarContrasena(request):

    reset_form = None
    if request.method == 'POST':
        data = None
        reset_form = PasswordResetForm(request.POST)
        if reset_form.is_valid():
            data = reset_form.cleaned_data["email"].lower().strip()
            usuario = User.objects.get(email=data)
            if usuario:
                body = render_to_string('correos/OlvidoContrasena.html', {'nombre': usuario.first_name,
                                                                                 'email': usuario.email,
                                                                                 'domain': request.META['HTTP_HOST'],
                                                                                 'uid': urlsafe_base64_encode(
                                                                                     force_bytes(usuario.pk)).decode(),
                                                                                 'token': default_token_generator.make_token(
                                                                                     usuario),
                                                                                 'protocol': 'http'
                                                                                 })
                email_message = EmailMessage(subject='Recuperar Contraseña', body=body,
                                             from_email=DEFAULT_FROM_EMAIL,
                                             to=[usuario.email])
                email_message.content_subtype = 'html'
                email_message.send()
                messages.add_message(request,messages.SUCCESS,'Se enviado un correo a : '+usuario.email)
                return redirect('login')

            else:
                messages.add_message(request, messages.ERROR, 'No pudimos encontrar el correo : '+usuario.email)
                return redirect('login')
    else:
        reset_form = PasswordResetForm()
    return render(request,'main/contrasena-olvidada.html',{'reset_form':reset_form})

