from django.contrib import admin

from .models import Oportunidad,BeneficioExtra,PesoCompatibilidadOportunidad,OportunidadCompatibilidad,ProcesoFase,Postulacion,ProcesoCompatibilidadOportunidades
# Register your models here.
admin.site.register(ProcesoFase)
admin.site.register(PesoCompatibilidadOportunidad),
admin.site.register(Oportunidad)
admin.site.register(Postulacion)
admin.site.register(BeneficioExtra)
admin.site.register(OportunidadCompatibilidad),
admin.site.register(ProcesoCompatibilidadOportunidades)
