from django.contrib import admin
from .models import Persona,Pais,Ciudad,GradoEstudio,NivelAcademico,Distrito,Universidad,RamaCarrera,Carrera,TipoCarrera,TipoPuesto,\
    TiempoExpeiencia,TipoRemuneracion,Beneficio,Idioma,IdiomaBase,AreaExpeiencia,CargaHoraria,Conocimiento,PeriodosGraduacion

admin.site.register(Persona)
admin.site.register(Pais)
admin.site.register(Ciudad)
admin.site.register(GradoEstudio)
admin.site.register(NivelAcademico)
admin.site.register(Distrito)
admin.site.register(Universidad)
admin.site.register(RamaCarrera)
admin.site.register(Carrera)
admin.site.register(TipoCarrera)
admin.site.register(TipoPuesto)
admin.site.register(TiempoExpeiencia)
admin.site.register(TipoRemuneracion)
admin.site.register(Beneficio)
admin.site.register(Idioma)
admin.site.register(IdiomaBase)
admin.site.register(AreaExpeiencia)
admin.site.register(CargaHoraria)
admin.site.register(Conocimiento)
admin.site.register(PeriodosGraduacion)