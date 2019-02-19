from django.urls import path,include
from .views import ListarOportunidades,VerOportunidad,VistaPrevia,CalificarPostulante
urlpatterns = [
    path('', ListarOportunidades ,name = 'index'),
    path('ver_oportunidad/<slug:slug>', VerOportunidad ,name = 'ver_oportunidad'),
    path('vista_previa/<int:id>', VistaPrevia ,name = 'vista_previa'),
    path('calificar/<int:id>/<int:valor>', CalificarPostulante ,name = 'calificar'),
]