# coding=utf-8
from datetime import date, datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import  HttpResponseRedirect

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

def calular_edad(born):
    if born is not None:
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    else:
        return 0

#carga el rago de años para el select
def anos_rango():
    anos = []
    today = date.today()
    desde = today.year - 16
    hasta = today.year+10
    for y in range(desde,hasta):
        anos.append((str(y), str(y)))
    return [('','Año')] + anos

#carga el rago de años para el select
def anos_experiencia():
    anos = []
    for y in range(2,11):
        anos.append((str(y), 'desde ' + str(y)+ 'años'))
    return [('','Año')]+ [('0','sin experiencia')]+ [('1','hasta 1 año')] + anos

#carga el rango de semestre para el  select
def semestre_rango():
    semestres = []

    semestres.append((str(1), "Enero"))
    semestres.append((str(2), "Febrero"))
    semestres.append((str(3), "Marzo"))
    semestres.append((str(4), "Abril"))
    semestres.append((str(5), "Mayo"))
    semestres.append((str(6), "Junio"))
    semestres.append((str(7), "Julio"))
    semestres.append((str(8), "Agosto"))
    semestres.append((str(9), "Setiembre"))
    semestres.append((str(10), "Octubre"))
    semestres.append((str(11), "Noviembre"))
    semestres.append((str(12), "Diciembre"))

    return semestres

#carga el rango de semestre para el  select
def semestre_carrera():
    semestres = []
    for y in range(1,11):
        semestres.append((str(y), "Ciclo " + str(y)))
    return semestres

#carga el rango de semestre para el  select
def dias_del_mes():
    dias = []
    for y in range(1,32):
        dias.append((y, y))
    return [('','Día')] + dias

def meses_del_ano():
    meses = []
    for y in range(1,13):
        meses.append((y, y))
    return [('','Mes')] + meses

def anos_nacimiento():
    anos = []
    for y in range(date.today().year - 36, (date.today().year - 17)):
        anos.append((y, y))
    return [('','Año')] + anos

def estado_oportunidad():
    anos = []
    anos.append(('P', 'Archivado'))
    anos.append(('A', 'Abierto'))
    anos.append(('C', 'Cerrado'))
    return anos

def estado_postulacion():
    anos = []
    anos.append(('P', 'Postulacion'))
    anos.append(('E', 'En Evaluacion'))
    anos.append(('F', 'Finalizado'))
    return anos

def estado_mensaje():
    anos = []
    anos.append(('G', 'Guardado'))
    anos.append(('E', 'Eliminado'))
    return anos

def estado_registro():
    anos = []
    anos.append(('A', 'Activo'))
    anos.append(('I', 'Inactivado'))
    return anos

def genero():
    anos = []
    anos.append(('M', 'Masculino'))
    anos.append(('F', 'Femenino'))
    return anos

def calificacion():
    calificaciones = []
    calificaciones.append(('SC', 'Sin Calificar'))
    calificaciones.append(('B','Bueno'))
    calificaciones.append(('MB', 'Muy Bueno'))
    calificaciones.append(('R', 'Regular'))
    return calificaciones
def rango_de_meses(fecha1, fecha2):
        return (fecha2.year - fecha1.year)*12 + fecha2.month - fecha1.month

def custom_redirect(url_name, **kwargs):
    from django.core.urlresolvers import reverse
    import urllib
    # url = reverse(url_name, args = args)
    params = urllib.urlencode(kwargs)
    return HttpResponseRedirect(url_name + "/?%s" % params)







