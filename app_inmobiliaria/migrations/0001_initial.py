# Generated by Django 5.0.2 on 2024-03-06 01:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('tipo_propiedad', models.CharField(choices=[('CASA', 'Casa'), ('DEPTO', 'Departamento')], max_length=10)),
                ('direccion', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metros_cuadrados', models.IntegerField(default=0)),
                ('habitaciones', models.IntegerField()),
                ('disponibilidad', models.CharField(choices=[('ALQUILER', 'Alquiler'), ('VENTA', 'Venta')], help_text='Selecciona si es para alquilar o venta', max_length=10)),
                ('descripcion', models.TextField()),
                ('fecha_publicacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField()),
                ('cliente_nombre', models.CharField(max_length=100)),
                ('cliente_email', models.EmailField(max_length=254)),
                ('comentarios', models.TextField(blank=True)),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inmobiliaria.agente')),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inmobiliaria.propiedad')),
            ],
        ),
        migrations.AddField(
            model_name='propiedad',
            name='propietario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_inmobiliaria.propietario'),
        ),
    ]