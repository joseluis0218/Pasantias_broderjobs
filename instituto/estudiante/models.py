from django.db import models
from users.models import User
from main.models import Persona, Pais, Ciudad, GradoEstudio, Universidad, Carrera, TipoPuesto, CargaHoraria, Idioma,\
    Conocimiento, AreaExpeiencia, Distrito, NivelAcademico
from empresas.models import Empresa, Puesto
from main import utils
from datetime import date, datetime

items_registro = utils.estado_registro()
class Estudiante(models.Model):
    items_ciclo = utils.semestre_rango()
    items_ciclo_carrera = utils.semestre_carrera()
    items_anos = utils.anos_rango()
    items_calificacion = utils.calificacion()
    persona = models.OneToOneField(Persona,on_delete=models.CASCADE)
    grado_estudio = models.ForeignKey(GradoEstudio,default=None, null=True, blank=True,on_delete=models.CASCADE )
    nivel_academico = models.ForeignKey(NivelAcademico,default=None, null=True, blank=True,on_delete=models.CASCADE )
    universidad = models.ForeignKey(Universidad,default=None, null=True, blank=True,on_delete=models.CASCADE )
    carrera = models.ForeignKey(Carrera, default=None, null=True, blank=True,on_delete=models.CASCADE )
    carrera_referencial = models.CharField(max_length=100, default=None, null=True, blank=True)
    semestre_actual = models.CharField(choices=items_ciclo_carrera, max_length=2, default=None, null=True, blank=True, )
    semestre_inicio_estudio = models.CharField(choices=items_ciclo,max_length=2, default=None, null=True, blank=True)
    ano_inicio_estudio = models.CharField(choices=items_anos, max_length=4, default=None, null=True,  blank=True, )
    semestre_graduacion = models.CharField(choices=items_ciclo, max_length=2, default=None, null=True, blank=True, )
    ano_graduacion= models.CharField(choices=items_anos, max_length=4, default=None, null=True, blank=True)
    pais = models.ForeignKey(Pais, default=None, null=True, blank=True,on_delete=models.CASCADE )
    ciudad = models.ForeignKey(Ciudad, default=None, null=True, blank=True,on_delete=models.CASCADE )
    distrito = models.ForeignKey(Distrito, default=None, null=True, blank=True,on_delete=models.CASCADE )
    carga_horaria = models.ForeignKey(CargaHoraria,default=None,null=True, blank=True,on_delete=models.CASCADE)
    tipo_puesto = models.ManyToManyField(TipoPuesto, default=None, blank=True, verbose_name="Tipo Puesto")
    idioma = models.ManyToManyField(Idioma, default=None, blank=True, verbose_name="Idioma")
    conocimiento = models.ManyToManyField(Conocimiento, default=None, blank=True, verbose_name="Conocimiento")
    remuneracion = models.CharField(max_length=50, default=None, null=True, blank=True)
    tiempo_experiencia = models.CharField(max_length=50, default=None, null=True, blank=True)
    foto = models.ImageField('foto perfil', upload_to='img/%Y/%m/%d', null=True, blank=True)
    foto_facebook_url =  models.URLField(default=None, null=True, blank=True)
    completo_test = models.BooleanField(default=False)
    correo_registro = models.BooleanField(default=False)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    enviado_correo_cargararea = models.BooleanField(default=False)

    def __str__(self):
	    return self.persona.usuario.first_name

    @property
    def set_foto(self):
        if self.foto:
            return self.foto.url
        else:
            if self.foto_facebook_url:
                return self.foto_facebook_url
            else:
                return "/static/img/profile/profile_default.png"


class Resumen(models.Model):
    estudiante =  models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    descripcion = models.TextField(default=None, null=True, blank=True)

    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __str__(self):
	    return self.estudiante.persona.usuario.first_name

class ActividadesExtra(models.Model):
    estudiante =  models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    descripcion = models.TextField(default=None, null=True, blank=True)
    organizacion = models.CharField(max_length=50, default=None, null=True, blank=True)

    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __str__(self):
	    return self.descripcion

class ExperienciaProfesional(models.Model):
    estudiante =  models.ForeignKey(Estudiante, default=None, null=True, blank=True,on_delete=models.CASCADE)
    puesto = models.ForeignKey(Puesto, default=None, null=True, blank=True,on_delete=models.CASCADE)
    area_experiencia =  models.ForeignKey(AreaExpeiencia, default=None, null=True, blank=True,on_delete=models.CASCADE)
    puesto_referencial = models.CharField(max_length=50, default=None, null=True)
    empresa = models.ForeignKey(Empresa, default=None, null=True, blank=True,on_delete=models.CASCADE)
    empresa_referencial = models.CharField(max_length=50, default=None, null=True)
    fecha_desde = models.DateField(default=None, null=True, blank=True)
    fecha_hasta = models.DateField(default=None, null=True, blank=True)
    trabajo_actual = models.CharField(max_length=1, default='N',)
    descripcion = models.TextField(default=None, null=True, blank=True)

    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __str__(self):
	    return self.puesto.descripcion

class Voluntariado(models.Model):
    estudiante =  models.ForeignKey(Estudiante, default=None, null=True, blank=True,on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50, default=None, null=True, blank=True)
    organizacion = models.CharField(max_length=50, default=None, null=True, blank=True)
    fecha_desde = models.DateField(null=True)
    fecha_hasta = models.DateField(default=None, null=True, blank=True)
    voluntariado_actual = models.CharField(max_length=1, default='N')
    descripcion = models.TextField(default=None, null=True, blank=True)

    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __str__(self):
	    return self.cargo


class ConocimientoExtra(models.Model):
    descripcion = models.CharField(max_length=50, default=None, null=True, blank=True)
    estudiante = models.ForeignKey(Estudiante, default=None, null=True, blank=True,on_delete=models.CASCADE)
    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
	    return self.descripcion