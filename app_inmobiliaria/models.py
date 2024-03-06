from django.db import models

# Create your models here.

class Propietario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return f"Propietario: {self.nombre} -- {self.apellido}"

class Propiedad(models.Model):
    TIPO_PROPIEDAD_CHOICES = [('CASA', 'Casa'),('DEPTO', 'Departamento'),]
    DISPONIBILIDAD_CHOICES = [('ALQUILER', 'Alquiler'),('VENTA', 'Venta'),]
    titulo = models.CharField(max_length=100)
    tipo_propiedad = models.CharField(max_length=10, choices=TIPO_PROPIEDAD_CHOICES)
    direccion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    metros_cuadrados = models.IntegerField(default=0)
    habitaciones = models.IntegerField()
    disponibilidad = models.CharField(max_length=10, choices=DISPONIBILIDAD_CHOICES, help_text="Selecciona si es para alquilar o venta")
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    propietario = models.ForeignKey(Propietario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Propiedad: {self.titulo} -- {self.direccion}"

class Agente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)    
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    descripcion = models.TextField()

    def __str__(self):
        return f"Agente: {self.nombre} - {self.apellido}"

class Cita(models.Model):
    fecha_hora = models.DateTimeField()
    cliente_nombre = models.CharField(max_length=100)
    cliente_email = models.EmailField()
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE)
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"Cita: {self.cliente_nombre} - {self.propiedad.titulo} -- Fecha: {self.fecha_hora}"    
     
    

