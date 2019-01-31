from django.urls import path,include
from .views import Principal
urlpatterns = [
    path('', Principal ,name = 'index'),
]