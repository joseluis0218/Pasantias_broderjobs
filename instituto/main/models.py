from django.db import models
from users.models import User
from datetime import date, datetime
from main import utils

items_registro = utils.estado_registro()

class Persona(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    telefono = models.CharField(default=None, null=True, blank=True, max_length=20)
    fecha_nacimiento = models.DateField(default=None, null=True, blank=True)
    tipo_persona = models.CharField(max_length=1, default="E")
    genero = models.CharField(choices=utils.genero(), max_length=1, default='', null=True, blank=True)
    dni = models.CharField(default=None, null=True, blank=True, max_length=20)
    enviar_correo = models.BooleanField(default=False, blank = True)
    fecha_creacion = models.DateField(default=  datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ["usuario"]

    def __str__(self):
        return self.usuario.first_name
class GradoEstudio(models.Model):
    descripcion = models.CharField(max_length=50)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion

class NivelAcademico(models.Model):
    descripcion = models.CharField(max_length=50)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion

class Pais(models.Model):
    descripcion = models.CharField(max_length=50)
    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(max_length=1, default='A', null=True, blank=True)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion

class Ciudad(models.Model):

    pais = models.ForeignKey(Pais,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)
    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado = models.CharField(max_length=1, default='A', null=True, blank=True)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion
class Distrito(models.Model):
    ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion

class Universidad(models.Model):
    descripcion = models.CharField(max_length=500, default=None, null=True, blank=True)
    nemonico = models.CharField(max_length=50, default=None, null=True, blank=True)
    pais = models.ForeignKey(Pais, default=None, null=True, blank=True,on_delete=models.CASCADE)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)
    tipo_carrera = models.ForeignKey('TipoCarrera', default=None, null=True, blank=True,on_delete=models.CASCADE)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion

class RamaCarrera(models.Model):
    descripcion = models.CharField(max_length=50, default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion

class TipoCarrera(models.Model):

    descripcion = models.CharField(max_length=50, default=None, null=True, blank=True)
    total_ciclos = models.IntegerField(null= True, blank= True, verbose_name='total de ciclos')

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden", "descripcion"]

    def __str__(self):
        return self.descripcion

class Carrera(models.Model):
    descripcion = models.CharField(max_length=50, default=None, null=True, blank=True)
    tipo_carrera = models.ForeignKey(TipoCarrera, default=None, null=True, blank=True,on_delete=models.CASCADE)
    rama_carrera = models.ManyToManyField(RamaCarrera, default=None, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)
    codigo_externo = models.CharField(max_length=20, default=None, null=True, blank=True)

    class Meta:
        ordering = ["orden", "descripcion"]

    def __str__(self):
        return self.descripcion

class TipoPuesto(models.Model):
    descripcion = models.CharField(max_length=50, default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden", "descripcion"]

    def __str__(self):
        return self.descripcion

class CargaHoraria(models.Model):
    descripcion = models.CharField(max_length=50, default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion

class IdiomaBase(models.Model):
    descripcion = models.CharField(max_length=50, default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion

class Idioma(models.Model):
    idiomabase = models.ForeignKey(IdiomaBase, default= None, null= True, blank= True,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50, default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion

class Conocimiento(models.Model):
    descripcion = models.CharField(max_length=50, default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion

class TipoRemuneracion(models.Model):
    descripcion = models.CharField(max_length=50, default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion

class Beneficio(models.Model):
    descripcion = models.CharField(max_length=50, default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion

class PeriodosGraduacion(models.Model):

    descripcion = models.CharField(max_length=50, default=None, null=True, blank=True)
    secuencia_universitaria = models.IntegerField(null= True, blank= True)
    secuencia_tecnica = models.IntegerField(null= True, blank= True)
    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion

class AreaExpeiencia(models.Model):
    descripcion = models.CharField(max_length=500, default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden","descripcion"]

    def __str__(self):
        return self.descripcion

class TiempoExpeiencia(models.Model):
    descripcion = models.CharField(max_length=500, default=None, null=True, blank=True)
    meses_tope = models.IntegerField(null= True, blank= True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden","descripcion"]

    def __str__(self):
        return self.descripcion
