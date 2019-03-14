from django.urls import path,include
from .views import ListarEmpresa,CambiarEstado
urlpatterns = [
    path('', ListarEmpresa ,name = 'index'),
    path('cambiar_estado/<int:id>', CambiarEstado ,name = 'cambiar_estado'),
]