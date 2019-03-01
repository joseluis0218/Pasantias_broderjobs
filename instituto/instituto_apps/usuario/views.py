
from django.shortcuts import render, redirect
from main.models import Persona
from users.models import User
from .forms import UsuarioForm,PersonaForm,UsuarioEditForm
from django.contrib import messages
from django.core.paginator import Paginator


def ListarUsuario(request):

    personas = Persona.objects.filter(tipo_persona = 'I', usuario__is_superuser = False)
    paginator = Paginator(personas, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    personas = paginator.get_page(page)

    return render(request, 'usuario/usuarios.html', {'personas' : personas})

def CrearUsuario(request):

    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        persona_form = PersonaForm(request.POST)
        if not request.is_ajax():
            print(request.POST)
            if usuario_form.is_valid() and persona_form.is_valid():
                usuario = usuario_form.save()
                persona = persona_form.save(commit=False)
                persona.usuario = usuario
                persona.tipo_persona = 'I'
                persona.save()
            # persona_form.save
                messages.add_message(request, messages.SUCCESS, 'Usuario registrado correctamente')
                return redirect('usuario:index')

    else:
        usuario_form = UsuarioForm()
        persona_form = PersonaForm()

    return render(request,'usuario/crear-usuario.html',{'usuario_form':usuario_form,'persona_form':persona_form})

def VerUsuario(request,id):
    persona_form = None
    usuario_form = None

    persona = Persona.objects.get(id=id)
    usuario = User.objects.get(id=persona.usuario.id)
    if request.method == 'GET':
        persona_form = PersonaForm(instance=persona)
        usuario_form = UsuarioForm(instance=usuario)
    return render(request,'usuario/ver-usuario.html',{'persona_form' : persona_form,'usuario_form': usuario_form})

def EditarUsuario(request,id):
    persona_form = None
    usuario_form = None
    persona = Persona.objects.get(id=id)
    usuario = User.objects.get(id=persona.usuario.id)

    if request.method == 'GET':
        persona_form = PersonaForm(instance=persona)
        usuario_form = UsuarioEditForm(instance=usuario)

    else:
        persona_form = PersonaForm(request.POST, instance=persona)
        usuario_form = UsuarioEditForm(request.POST, instance=usuario)
        if not request.is_ajax():
            if persona_form.is_valid() and usuario_form.is_valid():
                usuario_form.save()
                persona_form.save()
                print(request.POST)
                messages.add_message(request, messages.SUCCESS, 'Usuario actualizado correctamente')
            return redirect('usuario:index')

    return render(request, 'usuario/editar-usuario.html', {'persona_form': persona_form, 'usuario_form' : usuario_form})

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