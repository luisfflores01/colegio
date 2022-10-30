# Generated by Django 4.1.2 on 2022-10-30 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modulos.persona.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('persona', '0004_alter_tutor_celular_alter_tutor_fotografia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_eliminacion', models.DateTimeField(blank=True, null=True)),
                ('rude', models.CharField(max_length=20, unique=True, verbose_name='Nro. Rude')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellido_paterno', models.CharField(blank=True, max_length=50, null=True, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(blank=True, max_length=50, null=True, verbose_name='Apellido Materno')),
                ('documento', models.CharField(max_length=15, unique=True, verbose_name='Carnet de Identidad')),
                ('fotografia', models.ImageField(blank=True, max_length=200, null=True, upload_to='media/tutor/', verbose_name='Fotografía del Tutor(a)')),
                ('zona', models.CharField(max_length=50, verbose_name='Zona')),
                ('calleavenida', models.CharField(max_length=50, verbose_name='Calle /Avenida')),
                ('numero', models.CharField(blank=True, max_length=50, null=True, verbose_name='Número')),
                ('celular', models.IntegerField(default=0, validators=[modulos.persona.validators.validar_celular], verbose_name='Nro. Celular')),
                ('expedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='persona.departamento')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='persona.genero')),
                ('tipotutor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='persona.tipotutor')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_eliminacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
    ]