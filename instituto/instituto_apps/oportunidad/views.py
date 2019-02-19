from django.shortcuts import render,redirect
from oportunidades.models import Oportunidad,Postulacion,OportunidadCompatibilidad
from estudiante.models import Estudiante
from main.utils import calular_edad,estado_oportunidad
from main import utils
# Create your views here.

# def Principal(request):
#
#     return render(request, 'oportunidad/oportunidades.html')

def ListarOportunidades(request):

    oportunidades = Oportunidad.objects.all()

    oport_abiertas = Oportunidad.objects.filter(estado_oportunidad = 'A')
    oport_cerradas = Oportunidad.objects.filter(estado_oportunidad='C')
    oport_archivadas = Oportunidad.objects.filter(estado_oportunidad='P')

    # postu_muybuenos = Postulacion.objects.filter(estudiante_calificacion = 'MB').count()
    # postu_buenos = Postulacion.objects.filter(estudiante_calificacion = 'B').count()
    # postu_buenos = Postulacion.objects.filter(estudiante_calificacion = 'B').count()
    estados = ['A','C','P']
    for estado in estados:
        print(estado)
    # print(estados)
    for oportunidad in oportunidades:
        estado_oportunidad = oportunidad.estado_oportunidad
        # print(estado_oportunidad)
            # if oportunidad.estado_oportunidad == 'A':
            #     postu_muybuenos = Postulacion.objects.filter(oportunidad_id = oportunidad.id, estudiante_calificacion = 'MB').count()
            #     print(postu_muybuenos)

    return render(request,'oportunidad/oportunidades.html',{'oportunidades':oportunidades,'estado_oportunidad':estado_oportunidad,'oport_abiertas':oport_abiertas,'estados':estados,'oport_cerradas':oport_cerradas,
                                                            'oport_archivadas':oport_archivadas})
                                                            # 'muybuenos':postu_muybuenos,'buenos':postu_buenos,'regulares':postu_regulares})


def VerOportunidad(request,slug):
    if request.method == 'GET':
         oportunidad = Oportunidad.objects.get(slug=slug)
         postulantes = Postulacion.objects.filter(oportunidad_id = oportunidad.id, estado_postulacion = 'P').order_by('fecha_creacion')
         compatibilidades = OportunidadCompatibilidad.objects.filter(oportunidad_id = oportunidad.id)
         if(compatibilidades):
             for compatibilidad in compatibilidades:
                 compat_acedemica = compatibilidad.compatibilidad_academica
         else:
             compat_acedemica = 0
         if (postulantes):
            for postulante in postulantes:
                fecha_nac = postulante.estudiante.persona.fecha_nacimiento
                edad_postulante = calular_edad(fecha_nac)

         else:
             edad_postulante = 0
    return render(request,'oportunidad/ver-oportunidad.html',{'oportunidad':oportunidad,'postulantes' : postulantes,'compat_acedemica':compat_acedemica,'edad_postulante' : edad_postulante})

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
                print("cagon ctm")
                postulante.estudiante_calificacion = 'MB'
            elif valor == 2:
                postulante.estudiante_calificacion = 'B'
            elif valor == 3:
                postulante.estudiante_calificacion = 'R'
            else:
                postulante.estudiante_calificacion = 'SC'

            postulante.save()
            print(postulante.estudiante_calificacion)


    return redirect("oportunidad:index")