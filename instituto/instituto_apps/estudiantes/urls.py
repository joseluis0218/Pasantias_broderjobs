from django.urls import path,include
from .views import Index,BuscarCvs
urlpatterns = [
    path('', Index ,name = 'index'),
    path('buscar_cvs/', BuscarCvs ,name = 'buscar'),
]