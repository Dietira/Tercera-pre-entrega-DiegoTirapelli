from django import forms
from .models import *

class Formulario_Agente(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)    
    telefono = forms.CharField(max_length=20)
    email = forms.EmailField()
    descripcion = forms.CharField(widget=forms.Textarea, required=False)

class Formulario_Propietario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()

class Formulario_Propiedad(forms.Form):
    TIPO_PROPIEDAD_CHOICES = [('CASA', 'Casa'),('DEPTO', 'Departamento'),]
    DISPONIBILIDAD_CHOICES = [('ALQUILER', 'Alquiler'),('VENTA', 'Venta'),]
    titulo = forms.CharField(max_length=100)
    tipo_propiedad = forms.ChoiceField(choices=TIPO_PROPIEDAD_CHOICES)
    direccion = forms.CharField(max_length=100)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    metros_cuadrados = forms.IntegerField(initial=0)
    habitaciones = forms.IntegerField(initial=0)
    disponibilidad = forms.ChoiceField(choices=DISPONIBILIDAD_CHOICES)
    descripcion = forms.CharField(max_length=255, widget=forms.Textarea, required=False)
    fecha_publicacion = forms.DateField(widget=forms.SelectDateWidget)
    propietario = forms.ModelChoiceField(queryset=Propietario.objects.all())

class Formulario_Cita(forms.Form):
    fecha_hora = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'])
    cliente_nombre = forms.CharField(max_length=100)
    cliente_email = forms.EmailField()
    comentarios = forms.CharField(widget=forms.Textarea, required=False)
    propiedad = forms.ModelChoiceField(queryset=Propiedad.objects.all())
    agente = forms.ModelChoiceField(queryset=Agente.objects.all())

class BuscarPropiedadForm(forms.Form):
    TIPO_PROPIEDAD_CHOICES = [('', '---'), ('CASA', 'Casa'),('DEPTO', 'Departamento'),]
    DISPONIBILIDAD_CHOICES = [('', '---'), ('ALQUILER', 'Alquiler'), ('VENTA', 'Venta'),]    
    tipo_propiedad = forms.ChoiceField(choices=TIPO_PROPIEDAD_CHOICES, required=False)
    disponibilidad = forms.ChoiceField(choices=DISPONIBILIDAD_CHOICES, required=False)
