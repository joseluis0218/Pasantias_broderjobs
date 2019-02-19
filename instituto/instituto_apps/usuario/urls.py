from django.urls import path,include
from .views import ListarUsuario,CrearUsuario,EditarUsuario,VerUsuario,EliminarUsuario
urlpatterns = [
    path('', ListarUsuario ,name = 'index'),
    path('crear_usuario/', CrearUsuario ,name = 'crear_usuario'),
    path('editar_usuario/<int:id>', EditarUsuario ,name = 'editar_usuario'),
    path('ver_usuario/<int:id>', VerUsuario, name = 'ver_usuario'),
    path('eliminar_usuario/<int:id>', EliminarUsuario ,name = 'eliminar_usuario'),
]