from django.urls import path
from app_inmobiliaria.views import *

urlpatterns = [
    path('', inicio, name= "inicio"),
    path('propiedades/', propiedades, name="propiedades"),    
    path('propietarios/', propietarios, name= "propietarios"),
    path('agentes/', agentes, name="agentes"),
    path('citas/',citas, name= "citas"),    
    path('buscarPropiedades/',buscarPropiedades, name= "buscarPropiedades"),
]

