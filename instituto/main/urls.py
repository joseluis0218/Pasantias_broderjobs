from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import LoginInstituto,CrearUsuarioInstituto,VerificarCuenta,OlvidarContrasena
urlpatterns = [

    # path('home/',LoginInstituto, name = 'home'),
    path('login/', LoginInstituto ,name="login"),
    path('registrar_instituto/',CrearUsuarioInstituto,name = 'registrar'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name="logout"),
    path('verificar_cuenta/<uidb64>/<token>/',VerificarCuenta,name = "verificar_cuenta_instituto"),
    path('contrasena_crear/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='main/contrasena-restablecer.html',success_url='/login'),name='contrasena_crear'),
    path('contrasena_recuperar/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='main/contrasena-restablecer.html',success_url='/login'),name='contrasena_recuperar'),
    path('olvidar_contrasena/',OlvidarContrasena,name="olvidar_contrasena"),
    path('cambiar_contrasena/', auth_views.PasswordChangeView.as_view(template_name = 'main/cambiar-contrasena.html',success_url = 'hecho' ),name = 'cambiar_contrasena'),

    path('cambiar_contrasena/hecho', auth_views.PasswordChangeDoneView.as_view(template_name = 'main/cambiar-contrasena-hecho.html'),name = 'cambiar_contrasena_hecho')
]
