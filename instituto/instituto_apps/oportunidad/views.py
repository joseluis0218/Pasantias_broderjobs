from django.shortcuts import render,redirect
from oportunidades.models import Oportunidad,Postulacion,OportunidadCompatibilidad
from estudiante.models import Estudiante,Resumen,ExperienciaProfesional,ActividadesExtra
from main.utils import calular_edad,estado_oportunidad
from .forms import OportunidadForm,OportunidadCrearForm
from main import utils
from datetime import date, datetime,timedelta,time
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils.text import slugify
def ListarOportunidades(request):


    oport_abiertas = Oportunidad.objects.filter(estado_oportunidad = 'A')
    oport_cerradas = Oportunidad.objects.filter(estado_oportunidad='C')
    oport_archivadas = Oportunidad.objects.filter(estado_oportunidad='P')

    cantidad_abiertas = oport_abiertas.count()
    cantidad_cerradas = oport_cerradas.count()
    cantidad_archivadas = oport_archivadas.count()

    lista_abiertas = []
    lista_cerradas = []
    lista_archivadas = []

    for oport_abierta in oport_abiertas:
        postulantes_sv = Postulacion.objects.filter(oportunidad__id=oport_abierta.id, visto = 'False').count()
        postulantes_mb = Postulacion.objects.filter(oportunidad__id = oport_abierta.id, calificacion = 'MB').count()
        postulantes_b = Postulacion.objects.filter(oportunidad__id = oport_abierta.id, calificacion = 'B').count()
        postulantes_r = Postulacion.objects.filter(oportunidad__id=oport_abierta.id, calificacion='R').count()
        postulantes_sc = Postulacion.objects.filter(oportunidad__id=oport_abierta.id, calificacion='SC').count()
        lista_abiertas.append([oport_abierta, [postulantes_sv,postulantes_mb,postulantes_b,postulantes_r,postulantes_sc]])
    for oport_cerrada in oport_cerradas:
        postulantes_sv = Postulacion.objects.filter(oportunidad__id=oport_cerrada.id, visto = 'False').count()
        postulantes_mb = Postulacion.objects.filter(oportunidad__id = oport_cerrada.id, calificacion = 'MB').count()
        postulantes_b = Postulacion.objects.filter(oportunidad__id = oport_cerrada.id, calificacion = 'B').count()
        postulantes_r = Postulacion.objects.filter(oportunidad__id=oport_cerrada.id, calificacion='R').count()
        postulantes_sc = Postulacion.objects.filter(oportunidad__id=oport_cerrada.id, calificacion='SC').count()
        lista_cerradas.append([oport_cerrada, [postulantes_sv,postulantes_mb,postulantes_b,postulantes_r,postulantes_sc]])
    for oport_archivada in oport_archivadas:
        postulantes_sv = Postulacion.objects.filter(oportunidad__id=oport_archivada.id, visto = 'False').count()
        postulantes_mb = Postulacion.objects.filter(oportunidad__id = oport_archivada.id, calificacion = 'MB').count()
        postulantes_b = Postulacion.objects.filter(oportunidad__id = oport_archivada.id, calificacion = 'B').count()
        postulantes_r = Postulacion.objects.filter(oportunidad__id=oport_archivada.id, calificacion='R').count()
        postulantes_sc = Postulacion.objects.filter(oportunidad__id=oport_archivada.id, calificacion='SC').count()
        lista_archivadas.append([oport_archivada, [postulantes_sv,postulantes_mb,postulantes_b,postulantes_r,postulantes_sc]])

    return render(request,'oportunidad/oportunidades.html',{'cantidad_abiertas':cantidad_abiertas,'estados':estado_oportunidad,'cantidad_cerradas':cantidad_cerradas,'cantidad_archivadas':cantidad_archivadas, 'oport_abiertas': lista_abiertas, 'oport_cerradas': lista_cerradas, 'oport_archivadas': lista_archivadas})

def VerOportunidad(request,slug):
    if request.method == 'GET':
         oportunidad = Oportunidad.objects.get(slug=slug)
         postulaciones = Postulacion.objects.filter(oportunidad_id = oportunidad.id, estado_postulacion = 'P')
         # print(postulaciones)
         lista_compatibilidades = []
         for postulacion in postulaciones:
            compatibilidades = OportunidadCompatibilidad.objects.filter(estudiante_id = postulacion.estudiante.id)
            for compatibilidad in compatibilidades:
                fecha = postulacion.estudiante.persona.fecha_nacimiento
                edad = calular_edad(fecha)
                lista_compatibilidades.append([compatibilidad,postulacion,edad])
                print(postulacion)
            print(lista_compatibilidades)

    return render(request,'oportunidad/ver-oportunidad.html',{'oportunidad':oportunidad,'postulantes':lista_compatibilidades})

def VistaPrevia(request,id):
    if request.method == 'GET':
        oportunidad = Oportunidad.objects.get(id=id)

    return render(request, 'oportunidad/vista-previa.html',{'oportunidad':oportunidad})

def CalificarPostulante(request,id,valor):

    if request.method == 'POST':
        print(request.POST)
        if request.is_ajax():
            postulante = Postulacion.objects.get(id=id)

            print(valor)

            if valor == 1:
                postulante.calificacion = 'MB'
            elif valor == 2:
                postulante.calificacion = 'B'
            elif valor == 3:
                postulante.calificacion = 'R'
            else:
                postulante.calificacion = 'SC'

            postulante.save()
            print(postulante.calificacion)

    return redirect('oportunidad:index')
def VerCv(request,id):
    if request.method == 'GET':
        estudiante = Estudiante.objects.get(id = id)
        postulacion = Postulacion.objects.get(estudiante__id=estudiante.id)
        fecha_nac = estudiante.persona.fecha_nacimiento
        experiencias_profesionales = ExperienciaProfesional.objects.filter(estudiante_id=estudiante.id).order_by('-fecha_desde')
        actividades_extras = ActividadesExtra.objects.filter(estudiante_id = estudiante.id).order_by('-fecha_creacion')
        print(experiencias_profesionales)
        edad = calular_edad(fecha_nac)

        if postulacion.visto == False:
            postulacion.visto = True
            postulacion.save()
        try:
            resumen = Resumen.objects.get(estudiante__id=estudiante.id)
        except ObjectDoesNotExist as e:
            resumen = None
    return render(request,'oportunidad/estudiante-cv.html',{'estudiante':estudiante,'resumen':resumen,'edad':edad,'experiencias_profesionales':experiencias_profesionales,'actividades_extras':actividades_extras})

def AbrirOportunidad(request,id):
    oportunidad = Oportunidad.objects.get(id = id)

    print(date.today() + timedelta(days=10))
    if request.method == 'POST':
        oportunidad.estado_oportunidad = 'A'
        oportunidad.fecha_cese = date.today() + timedelta(days=10)
        oportunidad.save()
        return redirect('oportunidad:index')
    return render(request,'oportunidad/abrir-oportunidad.html',{'oportunidad':oportunidad})

def CerrarOportunidad(request,id):
    oportunidad = Oportunidad.objects.get(id = id)
    if request.method == 'POST':
        oportunidad.estado_oportunidad = 'C'
        oportunidad.fecha_cese = date.today()

        oportunidad.save()
        return redirect('oportunidad:index')
    return render(request,'oportunidad/cerrar-oportunidad.html',{'oportunidad':oportunidad})

def ArchivarOportunidad(request,id):
    oportunidad = Oportunidad.objects.get(id = id)
    postulaciones = Postulacion.objects.filter(oportunidad__id = oportunidad.id)
    print(postulaciones)
    if request.method == 'POST':
        oportunidad.estado_oportunidad = 'P'
        for postulante in postulaciones:
            postulante.delete()
        oportunidad.save()
        return redirect('oportunidad:index')
    return render(request,'oportunidad/archivar-oportunidad.html',{'oportunidad':oportunidad})


def EditarOportunidad(request, id):
    form = None
    oportunidad = Oportunidad.objects.get(id=id)
    if request.method == 'GET':
        form = OportunidadForm(instance=oportunidad)
    else:
        form = OportunidadForm(request.POST, instance=oportunidad)
        if not request.is_ajax():
            if form.is_valid():
                oportunidad.slug = slugify(oportunidad.titulo)
                form.save()
                print(request.POST)
                messages.add_message(request, messages.SUCCESS, 'Oportunidad actualizada correctamente')
            return redirect("oportunidad:index")
    return render(request,'oportunidad/editar-oportunidad.html',{'form': form})