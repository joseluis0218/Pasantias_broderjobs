from django.shortcuts import render,redirect
from empresas.models import Representante,Empresa
from main.models import Persona
from datetime import date, datetime
def ListarEmpresa(request):

    datos = Representante.objects.filter(persona__tipo_persona = 'R', persona__usuario__is_superuser = False)

    return render(request, 'empresa/empresas.html', {'datos': datos})

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
            else:
                representante.estado = 'A'
            representante.save()

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


def TraerData(request):

    print(request)
    return redirect("empresa:index")