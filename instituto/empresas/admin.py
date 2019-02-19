from django.contrib import admin
from .models import Empresa,Sector,FacturacionAnual,NumeroFuncionarios,Representante,Puesto,EmpresaDivision
# Register your models here.

admin.site.register(Sector)
admin.site.register(Puesto)
admin.site.register(NumeroFuncionarios)
admin.site.register(FacturacionAnual)
admin.site.register(Empresa)
admin.site.register(Representante)
admin.site.register(EmpresaDivision)