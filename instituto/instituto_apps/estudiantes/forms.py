
from django import forms

from main.models import RamaCarrera,GradoEstudio,TiempoExpeiencia,Ciudad,Persona
from django.forms.widgets import Textarea, RadioSelect, TextInput, DateInput, SelectMultiple, Select,CheckboxSelectMultiple,Input

class BuscarForm(forms.ModelForm):

    grado_estudio = forms.ModelChoiceField(queryset=GradoEstudio.objects.all(), empty_label="Grado Estudio",
                                           required=False, widget=forms.SelectMultiple(attrs={'class': 'select2 m-b-10 select2-multiple', 'style' : 'width:100%','multiple': 'multiple','data-placeholder':'Seleccione una o mas opciones','id' : 'select_grado'}))
    rama_carrera= forms.ModelMultipleChoiceField(queryset=RamaCarrera.objects.all(), required=False,
                                                 widget=forms.SelectMultiple(attrs={'class': 'select2 m-b-10 select2-multiple','style' : 'width:100%','multiple': 'multiple','data-placeholder':'Seleccione una o mas opciones','id' : 'select_rama'}))
    tiempo_experiencia = forms.ModelMultipleChoiceField(queryset=TiempoExpeiencia.objects.all(), required=False,
                                            widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Seleccione una o mas opciones','id' : 'select_tiempo'}))
    ciudad = forms.ModelMultipleChoiceField(queryset=Ciudad.objects.all(), required=False,
                                                  widget=forms.SelectMultiple(attrs={'class': 'select2 m-b-10 select2-multiple','style' : 'width:100%','multiple': 'multiple','data-placeholder':'Seleccione una o mas opciones','id' : 'select_ciudad'}))

    class Meta:
        model = Persona
        fields = ['genero']
        widgets = {
            'genero': Select(attrs={'class': 'form-control','id' : 'select_genero'}),
        }
    def __init__(self, *args, **kwargs):
        super(BuscarForm, self).__init__(*args, **kwargs)
        self.fields['tiempo_experiencia'].empty_label = "Tiempo experiencia"