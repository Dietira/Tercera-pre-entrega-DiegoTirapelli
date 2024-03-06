from django.shortcuts import render
from django.http import HttpResponse
from app_inmobiliaria.models import *
from app_inmobiliaria.forms import *

# Create your views here.
def inicio(request):
    return render(request, 'app_inmobiliaria/inicio.html')


def agentes(request):
    if request.method == 'POST':
        formAge = Formulario_Agente(request.POST)
        
        if formAge.is_valid():
            info = formAge.cleaned_data

            p = Agente(nombre=info["nombre"],
                           apellido=info["apellido"],
                           telefono=info["telefono"],                           
                           email=info["email"],
                           descripcion=info["descripcion"],
                           )
            p.save()
            formAge = Formulario_Agente()
    else:
        formAge = Formulario_Agente()
    
    return render(request, 'app_inmobiliaria/agentes.html',{"form1":formAge})

def propietarios(request):
    if request.method == 'POST':
        fPropietario = Formulario_Propietario(request.POST)
        if fPropietario.is_valid():
            info = fPropietario.cleaned_data
            p = Propietario(nombre=info["nombre"],
                                      apellido=info["apellido"],
                                      email=info["email"],
                            )
            p.save()
            fPropietario = Formulario_Propietario()
    else:
        fPropietario = Formulario_Propietario()
    
    return render(request, 'app_inmobiliaria/propietarios.html', {"form2": fPropietario})


def propiedades(request):
    if request.method == 'POST':
        fPropiedad = Formulario_Propiedad(request.POST)
        if fPropiedad.is_valid():
            info = fPropiedad.cleaned_data
            p = Propiedad(titulo =info["titulo"],
                          tipo_propiedad=info["tipo_propiedad"],
                          direccion=info["direccion"],
                          precio=info["precio"],
                          metros_cuadrados=info["metros_cuadrados"],
                          habitaciones=info["habitaciones"],
                          disponibilidad=info["disponibilidad"],
                          descripcion=info["descripcion"],
                          fecha_publicacion =info["fecha_publicacion"],
                          propietario=info["propietario"],
                          )
            p.save()
            fPropiedad = Formulario_Propiedad()
    else:
        fPropiedad = Formulario_Propiedad()
    
    return render(request, 'app_inmobiliaria/propiedades.html', {"form3": fPropiedad})

def citas(request):
    if request.method == 'POST':
        fCita = Formulario_Cita(request.POST)
        if fCita.is_valid():
            info = fCita.cleaned_data
            p = Cita(fecha_hora=info["fecha_hora"],
                            cliente_nombre=info["cliente_nombre"],
                            cliente_email=info["cliente_email"],
                            comentarios=info["comentarios"],
                            propiedad=info["propiedad"],
                            agente= info["agente"],
                            )
            p.save()
            fCita = Formulario_Cita()
    else:
        fCita = Formulario_Cita()
    
    return render(request, 'app_inmobiliaria/citas.html', {"form4": fCita})

def buscarPropiedades(request):
    propiedades = None
    if request.method == 'POST':
        form = BuscarPropiedadForm(request.POST)
        if form.is_valid():
            tipo_propiedad = form.cleaned_data['tipo_propiedad']
            disponibilidad = form.cleaned_data['disponibilidad']
            if tipo_propiedad and disponibilidad:
                propiedades = Propiedad.objects.filter(tipo_propiedad=tipo_propiedad, disponibilidad=disponibilidad)
            elif tipo_propiedad:
                propiedades = Propiedad.objects.filter(tipo_propiedad=tipo_propiedad)
            elif disponibilidad:
                propiedades = Propiedad.objects.filter(disponibilidad=disponibilidad)
    else:
        form = BuscarPropiedadForm()

    return render(request, 'app_inmobiliaria/buscarPropiedades.html', {'form5': form, 'propiedades': propiedades})

