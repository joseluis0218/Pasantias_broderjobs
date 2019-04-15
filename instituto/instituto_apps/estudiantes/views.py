from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from users.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from main.models import RamaCarrera,GradoEstudio
from oportunidades.models import OportunidadCompatibilidad
from estudiante.models import Estudiante
from .forms import BuscarForm
import json
@login_required(login_url='login')
def Index(request):
    form = BuscarForm()
    return render(request, 'estudiante/buscar-cvs.html',{'form' : form})


def BuscarCvs(request):
    if request.method == 'POST':
        if request.is_ajax():
            rama = request.POST['rama']
            print(type(rama))
            # grado_estudio = request.POST['grado_estudio']
            # genero = request.POST['genero']
            # ciudad = request.POST['ciudad']
            # tiempo_experiencia = request.POST['tiempo']
            estudiantes = Estudiante.objects.filter(carrera__rama_carrera__descripcion = rama)
            print(estudiantes)
            estudiantes = [cv_serializer(estudiante) for estudiante in estudiantes]

            return HttpResponse(json.dumps(estudiantes),content_type='application/json')

    return redirect('estudiante:index')




def cv_serializer(estudiante):

    nombres = estudiante.persona.usuario.first_name + ' ' + estudiante.persona.usuario.last_name
    compatibilidad = OportunidadCompatibilidad.objects.get(estudiante__id = estudiante.id)
    return {'nombres' : nombres,'universidad' : estudiante.universidad.descripcion,'carrera':estudiante.carrera.descripcion}