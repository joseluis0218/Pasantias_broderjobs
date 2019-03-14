from django.db import models
from users.models import User
from main.models import Persona,Pais, Ciudad
from datetime import date, datetime
from main import utils
from instituto.settings import STATIC_URL
items_registro = utils.estado_registro()

class Sector(models.Model):
    descripcion = models.CharField(max_length=50)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(max_length=1, default='A', null=True, blank=True)
    orden = models.IntegerField(null= True, blank= True)

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'
        ordering = ["descripcion"]

    def __str__(self):
        return self.descripcion

class Puesto(models.Model):
    descripcion = models.CharField(max_length=50)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion

class NumeroFuncionarios(models.Model):
    descripcion = models.CharField(max_length=50)

    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(max_length=1, default='A', null=True, blank=True)
    orden = models.IntegerField(null= True, blank= True)
    class Meta:
        verbose_name = 'NumeroFuncionario'
        verbose_name_plural = 'NumeroFuncionarios'
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion

class FacturacionAnual(models.Model):
    descripcion = models.CharField(max_length=50)

    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(max_length=1, default='A', null=True, blank=True)
    orden = models.IntegerField(null= True, blank= True)
    class Meta:
        verbose_name = 'FacturacionAnual'
        verbose_name_plural = 'FacturacionesAnuales'
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion

class Empresa(models.Model):

    nombre =  models.CharField(max_length=1000, default=None, null=True, blank=True)
    descripcion = models.CharField(max_length=200, default=None, null=True, blank=True)
    quienes_somos = models.CharField(max_length=1000, default=None, null=True, blank=True)
    telefono = models.CharField(max_length=100, default=None, null=True, blank=True)
    RUC = models.CharField(max_length=20, default=None, null=True, blank=True)
    sector = models.ForeignKey(Sector, default=None, null=True, blank=True,on_delete=models.CASCADE)
    numero_funcionarios = models.ForeignKey(NumeroFuncionarios, default=None, null=True, blank=True,on_delete=models.CASCADE)
    facturacion_anual = models.ForeignKey(FacturacionAnual, default=None, null=True, blank=True,on_delete=models.CASCADE)
    ano_fundacion =  models.CharField(max_length=10, default=None, null=True, blank=True)
    pais = models.ForeignKey(Pais, default=None, null=True, blank=True,on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, default=None, null=True, blank=True,on_delete=models.CASCADE)
    website = models.CharField(max_length=50, default=None, null=True, blank=True)
    logo = models.ImageField('logo', upload_to='img/%Y/%m/%d', null=True, blank=True)
    direccion_map = models.CharField(max_length=100, default=None, null=True, blank=True)
    longitud = models.FloatField(verbose_name='longitud', default=None, null=True, blank=True)
    latitud = models.FloatField(verbose_name='latitud', default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    usuario_creacion = models.CharField(max_length=50, default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length=50, default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ["orden"]

    def __str__(self):
        return self.nombre
    @property
    def set_logo(self):
        if self.logo:
            return self.logo.url
        else:
            return STATIC_URL+"img/profile/profile_default.png"

class Representante(models.Model):

    persona = models.OneToOneField(Persona,on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    administrador = models.BooleanField(default=False, blank=True)
    usuario_broder = models.BooleanField(default=False, blank=True)

    usuario_creacion = models.CharField(max_length=50, default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length=50, default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __str__(self):
        return self.persona.usuario.first_name

class EmpresaDivision(models.Model):
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)

    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)
    orden = models.IntegerField(null= True, blank= True)
    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.descripcion