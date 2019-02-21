from django.urls import path,include
from .views import ListarOportunidades,VerOportunidad,VistaPrevia,CalificarPostulante,VerCv,AbrirOportunidad,CerrarOportunidad,ArchivarOportunidad
urlpatterns = [
    path('', ListarOportunidades ,name = 'index'),
    path('ver_oportunidad/<slug:slug>', VerOportunidad ,name = 'ver_oportunidad'),
    path('vista_previa/<int:id>', VistaPrevia ,name = 'vista_previa'),
    path('calificar/<int:id>/<int:valor>', CalificarPostulante ,name = 'calificar'),
    path('abrir_oportunidad/<int:id>', AbrirOportunidad ,name = 'abrir_oportunidad'),
    path('cerrar_oportunidad/<int:id>', CerrarOportunidad ,name = 'cerrar_oportunidad'),
    path('archivar_oportunidad/<int:id>', ArchivarOportunidad ,name = 'archivar_oportunidad'),
    path('ver_cv/<int:id>', VerCv ,name = 'ver_cv'),
]