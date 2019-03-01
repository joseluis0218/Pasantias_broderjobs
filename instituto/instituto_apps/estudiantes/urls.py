from django.urls import path,include
from .views import BuscarCvs
urlpatterns = [
    path('', BuscarCvs ,name = 'index'),
]