# Tercera-pre-entrega-DiegoTirapelli

## Plataforma de Gestión Inmobiliaria

## Descripción
Esta aplicación web desarrollada con Django permite a los usuarios gestionar propiedades, agentes y propietarios, como así tambien programar citas.

## Características
- **Registro y gestión de propiedades**: Permite a los usuarios añadir propiedades.
- **Gestión de agentes y propietarios**: Los usuarios pueden registrar la información de agentes y propietarios.
- **Programación de citas**: Permite la creación de citas entre clientes y agentes inmobiliarios para ver una propiedad.
- **Búsqueda de propiedades**: Los usuarios pueden buscar propiedades por tipo y disponibilidad.

## Tecnologías Utilizadas
- **Python**: 3.10.7
- **Django**: 5.0.2

## Configuración del Proyecto
Para configurar y ejecutar el proyecto en tu entorno local, sigue estos pasos:

1. Realiza las migraciones para configurar la base de datos:

    python manage.py makemigrations 

    python manage.py migrate

2. Si lo deseas puedes crear un superusuario para acceder al panel de administración de Django:

    python manage.py createsuperuser

3. Inicia el servidor de desarrollo:

    python manage.py runserver

## URLs de la Aplicación
Para acceder a las diferentes secciones de la aplicación, utiliza las siguientes URLs:

- **Inicio**: `app_inmobiliaria/` - Página principal de la aplicación.
- **Propiedades**: `app_inmobiliaria/propiedades/` - Para registrar propiedades.
- **Propietarios**: `app_inmobiliaria/propietarios/` - Para registrar propietarios.
- **Agentes**: `app_inmobiliaria/agentes/` - Para registrar agentes inmobiliarios.
- **Citas**: `app_inmobiliaria/citas/` - Para programar una cita con el fin de conocer la propiedad.
- **Buscar Propiedades**: `app_inmobiliaria/buscarPropiedades/` - Para buscar propiedades según tipo y disponibilidad.

## Uso de la Aplicación
Navega por las URLs indicadas para acceder a las diferentes funcionalidades de la aplicación. Sigue las instrucciones en pantalla para realizar las acciones deseadas, como registrar propiedades o programar citas.

