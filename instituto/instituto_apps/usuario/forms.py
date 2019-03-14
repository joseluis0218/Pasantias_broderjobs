from django import forms

from users.models import User

from django.contrib.auth.forms import UserCreationForm
from main.models import Persona
from django.forms.widgets import Input
from django.core.exceptions import ValidationError
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
class PersonaForm(forms.ModelForm):
    telefono = forms.CharField()
    dni = forms.IntegerField(required=False)
    class Meta:
        model = Persona
        fields = ['telefono','fecha_nacimiento','dni','genero']
        widgets = {
            'fecha_nacimiento' : Input(attrs={'type' : 'date'}),
        }


class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']