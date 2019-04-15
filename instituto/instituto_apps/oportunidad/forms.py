# coding=utf-8
from django import forms
from django.forms.widgets import Textarea, RadioSelect, TextInput, DateInput, SelectMultiple, Select,CheckboxSelectMultiple,Input
from oportunidades.models import Oportunidad, TipoPuesto, CargaHoraria, Universidad, Idioma, Conocimiento, Beneficio, GradoEstudio, \
    TipoRemuneracion, Carrera, Pais, AreaExpeiencia, TiempoExpeiencia,Ciudad
from empresas.models import Representante, EmpresaDivision
from main.utils import genero




class OportunidadForm(forms.ModelForm):

    class Meta:
        model = Oportunidad
        fields = ('titulo', 'carga_horaria', 'remuneracion', 'remuneracion_min', 'remuneracion_max','ciudad','pais','distrito',
                  'fecha_cese', 'resumen','edad_desde', 'edad_hasta', 'genero', 'carga_horaria', 'tipo_puesto', 'estado', 'estado_oportunidad',
                  'grado_estudio', 'idioma', 'conocimiento', 'carrera', 'direccion_map', 'longitud', 'latitud',
                  'tipo_carrera', 'rama_carrera', 'area_experiencia', 'tiempo_experiencia', 'numero_vacantes', 'beneficio', 'nivel_academico')
        widgets = {
            'titulo': TextInput(attrs={'placeholder': 'Escriba el título de su vacante', 'class': 'form-control'}),
            'carga_horaria': RadioSelect(attrs={'class': 'form-check-input'}),
            'tipo_puesto': RadioSelect(attrs={'class': 'form-check-input', 'required':'required'}),
            'remuneracion': RadioSelect(attrs={'class': 'form-check-input'}),
            'resumen': Textarea(attrs={'class': 'form-control','required':'required'}),
            'remuneracion_min': TextInput(attrs={'placeholder': 'Valor mínimo','class': 'form-control'}),
            'remuneracion_max': TextInput(attrs={'placeholder': 'Valor máximo','class': 'form-control'}),
            'fecha_cese': Input(attrs={'type' : 'date','class': 'form-control'}),
            'direccion_map': TextInput(attrs={'placeholder': 'Dirección', 'class': 'form-control'}),
            'distrito': Select(attrs={'class': 'form-control'}),
            'pais': Select(attrs={'class': 'form-control'}),
            'ciudad': Select(attrs={'class': 'form-control'}),
            'rama_carrera': SelectMultiple(attrs={'class': 'select2 m-b-10 select2-multiple','style': 'width:100%;','multiple': 'multiple','required':'required','data-placeholder': 'Seleccione una o más opciones'}),
            'idioma': SelectMultiple(attrs={'class': 'select2 m-b-10 select2-multiple','style': 'width:100%;','multiple': 'multiple','data-placeholder': 'Seleccione una o más opciones'}),
            'grado_estudio': CheckboxSelectMultiple(attrs={'class': 'form-check-input','required':'required'}),
            'nivel_academico': CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'conocimiento': SelectMultiple(attrs={'class': 'select2 m-b-10 select2-multiple','style': 'width:100%;','multiple': 'multiple','data-placeholder': 'Seleccione una o más opciones'}),
            'estado_oportunidad': Select(attrs={'class': 'form-control','disabled':'disabled'}),
            'edad_desde': TextInput(attrs={'class': 'form-control', 'placeholder': 'Desde', 'type': 'number'}),
            'edad_hasta': TextInput(attrs={'class': 'form-control', 'placeholder': 'Hasta', 'type': 'number'}),
            'numero_vacantes': TextInput(attrs={'class': 'form-control','placeholder': 'Número de vacantes', 'type': 'number', 'value': '0'}),
            'genero': Select(attrs={'class': 'form-control'}),
            'division': Select(attrs={'class': 'form-control'}),
            'area_experiencia': Select(attrs={'class': 'form-control'}),
            'tiempo_experiencia': Select(attrs={'class': 'form-control'}),
            'beneficio': CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(OportunidadForm, self).__init__(*args, **kwargs)
        self.fields['carga_horaria'].empty_label = None
        self.fields['tipo_puesto'].empty_label = None
        self.fields['remuneracion'].empty_label = None
        self.fields['grado_estudio'].empty_label = None
        self.fields['nivel_academico'].empty_label = None
        self.fields['beneficio'].empty_label = None
        self.fields['distrito'].empty_label = "Distrito"
        self.fields['ciudad'].empty_label = "Ciudad"
        self.fields['genero'].empty_label = "Indiferente"
        self.fields['area_experiencia'].empty_label = "Área"
        self.fields['tiempo_experiencia'].empty_label = "Tiempo"


class OportunidadCrearForm(OportunidadForm):

    grado_estudio = forms.ModelChoiceField(queryset=GradoEstudio.objects.all(), empty_label="Grado Estudio", required = False, widget=forms.Select(attrs={'class': 'full', }))
    universidad = forms.ModelMultipleChoiceField(queryset=Universidad.objects.all(), required = False, widget=forms.SelectMultiple(attrs={'class': 'full actualizar', }))
    idioma = forms.ModelMultipleChoiceField(queryset= Idioma.objects.all(), required = False, widget=forms.SelectMultiple(attrs={'class': 'full actualizar', }))
    conocimiento = forms.ModelMultipleChoiceField(queryset=Conocimiento.objects.all(),  required = False, widget=forms.SelectMultiple(attrs={'class': 'full actualizar', }))
    carrera = forms.ModelMultipleChoiceField(queryset=Carrera.objects.all(),  required = False, widget=forms.SelectMultiple(attrs={'class': 'full actualizar', }))



