from django.contrib import admin
from django.db import models
from main.models import Persona, Pais, Ciudad, GradoEstudio, Universidad, Carrera, TipoPuesto, CargaHoraria, Idioma, \
    Conocimiento, TipoRemuneracion, Beneficio, PeriodosGraduacion, TipoCarrera, RamaCarrera, AreaExpeiencia, TiempoExpeiencia, NivelAcademico,Distrito
from empresas.models import Empresa, EmpresaDivision
from estudiante.models import Estudiante
from django.contrib.auth.models import User
from instituto.utils import unique_slugify

from main import utils


items_registro = utils.estado_registro()

class ProcesoFase(models.Model):

    descripcion = models.CharField(max_length=50, default=None, null=True, blank=True,  )
    orden = models.IntegerField(default=None, null=True, blank=True )
    mensaje_contenido = models.TextField(default=None, null=True, blank=True,  )
    mensaje_asunto = models.CharField(max_length=100, default=None, null=True, blank=True,  )

    usuario_creacion = models.CharField(max_length=50, default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length=50, default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __str__(self):
	    return self.descripcion

class PesoCompatibilidadOportunidad(models.Model):

    rama_carrera = models.FloatField(default=None, null=True, blank=True )
    universidad = models.FloatField(default=None, null=True, blank=True )
    grado_estudio = models.FloatField(default=None, null=True, blank=True )
    periodo_graduacion = models.FloatField(default=None, null=True, blank=True )
    edad = models.FloatField(default=None, null=True, blank=True )
    ubicacion = models.FloatField(default=None, null=True, blank=True )
    genero = models.FloatField(default=None, null=True, blank=True )
    tipo_puesto = models.FloatField(default=None, null=True, blank=True )
    carga_horaria = models.FloatField(default=None, null=True, blank=True )
    remuneracion = models.FloatField(default=None, null=True, blank=True )
    idioma = models.FloatField(default=None, null=True, blank=True )
    conocimiento = models.FloatField(default=None, null=True, blank=True )
    area_experiencia = models.FloatField(default=None, null=True, blank=True )
    tiempo_experiencia = models.FloatField(default=None, null=True, blank=True )
    ciclo_actual = models.FloatField(default=None, null=True, blank=True )
    experiencia = models.FloatField(default=None, null=True, blank=True )

    usuario_creacion = models.CharField(max_length=50, default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length=50, default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)


    def __str__(self):
	    return 'Registro de Peso'

class Oportunidad(models.Model):
    items_estado = utils.estado_oportunidad()
    genero = utils.genero()
    anos_experiencia = utils.anos_experiencia()
    # periodo= []
    # for e in PeriodosGraduacion.objects.all():
    #     periodo.append((str(e.valor), e.descripcion))

    empresa = models.ForeignKey(Empresa, default=None, null=True, blank=True,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, default=None, null=True, blank=True )
    carga_horaria = models.ForeignKey(CargaHoraria, default=None, null=True, blank=True, verbose_name="Jornada Laboral",on_delete=True)
    pais = models.ForeignKey(Pais, null=True, blank=True,on_delete=models.CASCADE)
    distrito = models.ForeignKey(Distrito, null=True, blank=True, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, null=True, blank=True,on_delete=models.CASCADE)
    remuneracion = models.ForeignKey(TipoRemuneracion, default=None, null=True, blank=True, verbose_name="Tipo de Remuneracion",on_delete=models.CASCADE)
    remuneracion_min = models.CharField(max_length=50, default=None, null=True, blank=True)
    remuneracion_max = models.CharField(max_length=50, default=None, null=True, blank=True)
    tipo_puesto = models.ForeignKey(TipoPuesto,default=None, null=False, blank=False, verbose_name="Tipo Puesto",on_delete=models.CASCADE)
    beneficio = models.ManyToManyField(Beneficio, default=None, blank=True, verbose_name="Beneficios")
    resumen = models.TextField(default=None, null=False, blank=False)
    estado_oportunidad =  models.CharField(choices=items_estado, max_length=1, default=None, null=True, blank=True)
    direccion_map = models.CharField(max_length=100, default=None, null=True, blank=True)
    longitud = models.FloatField(verbose_name='longitud', default=None, null=True, blank=True )
    latitud = models.FloatField(verbose_name='latitud', default=None, null=True, blank=True )
    grado_estudio = models.ManyToManyField(GradoEstudio, default=None, blank=False, verbose_name="grado estudios")
    universidad = models.ManyToManyField(Universidad, default=None, blank=True, verbose_name="universidad")
    tipo_carrera = models.ForeignKey(TipoCarrera, default=None, null=True, blank=True,on_delete=models.CASCADE)
    carrera = models.ManyToManyField(Carrera, default=None, blank=True, verbose_name="carrera")
    rama_carrera = models.ManyToManyField(RamaCarrera, default=None, blank=False, verbose_name="rama carrera")
    idioma = models.ManyToManyField(Idioma, default=None, blank=True, verbose_name="Idioma")
    conocimiento = models.ManyToManyField(Conocimiento, default=None, blank=True, verbose_name="Conocimiento")
    experiencia = models.CharField(choices=anos_experiencia, max_length=1, default=None, null=True, blank=True)
    direccion_map = models.CharField(max_length=100, default=None, null=True, blank=True)
    longitud = models.FloatField(verbose_name='longitud', default=None, null=True, blank=True )
    latitud = models.FloatField(verbose_name='latitud', default=None, null=True, blank=True )
    fecha_publicacion = models.DateField(default=None,null=True, blank=True)
    fecha_cese = models.DateField(default=None,null=True, blank=True )
    graduacion_desde = models.ForeignKey(PeriodosGraduacion, default=None,  null=True, blank=True, related_name="graduacion_desde",on_delete=models.CASCADE)
    graduacion_hasta = models.ForeignKey(PeriodosGraduacion, default=None,  null=True, blank=True, related_name="graduacion_hasta",on_delete=models.CASCADE)
    edad_desde = models.IntegerField(default=None, null=True, blank=True)
    numero_vacantes = models.IntegerField(default=None, null=True, blank=True)
    edad_hasta = models.IntegerField(default=None, null=True, blank=True)
    genero = models.CharField(choices=genero, max_length=1, default=None, null=True, blank=True)
    fase = models.ForeignKey(ProcesoFase, default=None, null=True, blank=True,on_delete=models.CASCADE)
    division = models.ForeignKey(EmpresaDivision, default=None, null=True, blank=True,on_delete=models.CASCADE)
    area_experiencia =  models.ForeignKey(AreaExpeiencia, default=None, null=True, blank=True,on_delete=models.CASCADE)
    tiempo_experiencia =  models.ForeignKey(TiempoExpeiencia, default=None, null=True, blank=True,on_delete=models.CASCADE)

    usuario_creacion = models.CharField(max_length=50, default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length=50, default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    notificacion_enviada = models.BooleanField(default=False, verbose_name="Notificacion enviada")
    nivel_academico = models.ManyToManyField(NivelAcademico, default=None, blank=True, verbose_name="nivel academico")

    url_imagen_empresa_correo =  models.URLField(default=None, null=True, blank=True)

    #Then override models save method:
    def save(self, *args, **kwargs):
        if not self.id:
            #Only set the slug when the object is created.
            # self.slug = slugify(self.titulo) #Or whatever you want the slug to use
            slug = '%s' % (self.titulo)
            unique_slugify(self, slug)
        super(Oportunidad, self).save(*args, **kwargs)


    def __str__(self):
	    return self.titulo

class Postulacion(models.Model):
    items_estado = utils.estado_postulacion()
    items_calificacion = utils.calificacion()
    oportunidad = models.ForeignKey(Oportunidad, default=None, null=True, blank=True,on_delete=True)
    estudiante = models.ForeignKey(Estudiante, default=None, null=True, blank=True,on_delete=True)
    estado_postulacion =  models.CharField(choices=items_estado, max_length=1, default='A', null=True, blank=True)
    fase = models.ForeignKey(ProcesoFase, default=None, null=True, blank=True,on_delete=True)
    estado_fase =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)
    calificacion = models.CharField(choices=items_calificacion, max_length=2, default='SC', null=True,blank=True)  # nuevo campo de calificación, maneja 3 tipos de califaiciones
    usuario_creacion = models.CharField(max_length=50, default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length=50, default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)
    visto = models.BooleanField(default=False, verbose_name="Postulacion Vista")

    def __str__(self):
	    return self.estudiante.persona.usuario.first_name

class BeneficioExtra(models.Model):
    descripcion = models.CharField(max_length=50, default=None, null=True, blank=True)
    oportunidad = models.ForeignKey(Oportunidad, default=None, null=True, blank=True,on_delete=True)
    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
	    return self.descripcion

class OportunidadCompatibilidad(models.Model):
    oportunidad = models.ForeignKey(Oportunidad, default=None, null=True, blank=True,on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, default=None, null=True, blank=True,on_delete=models.CASCADE)
    compatibilidad_academica = models.IntegerField(default=0, null= True, blank= True)
    compatibilidad_cultural = models.IntegerField(default=0, null= True, blank= True)
    compatibilidad_promedio = models.IntegerField(default=0, null= True, blank= True)
    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
	    return self.oportunidad.titulo+ '-'+self.estudiante.persona.usuario.first_name

class ProcesoCompatibilidadOportunidades(models.Model):
    procesar = models.BooleanField(default=False, blank=True, verbose_name="Seleccione y guarde para procesar "
                                                                               "la compatibilidad de todas las oportunidades")
    def __str__(self):
	    return 'Procesar Compatibilidades Oportunidades'