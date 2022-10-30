# Generated by Django 4.1.2 on 2022-10-30 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('persona', '0002_especialidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_eliminacion', models.DateTimeField(blank=True, null=True)),
                ('sigla', models.CharField(max_length=10, unique=True, verbose_name='Sigla')),
                ('departamento', models.CharField(max_length=20, verbose_name='Departamento')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_eliminacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_eliminacion', models.DateTimeField(blank=True, null=True)),
                ('genero', models.CharField(max_length=10, unique=True, verbose_name='Genero')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_eliminacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_eliminacion', models.DateTimeField(blank=True, null=True)),
                ('documento', models.CharField(max_length=15, unique=True, verbose_name='Carnet de Identidad')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellido_paterno', models.CharField(blank=True, max_length=50, null=True, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(blank=True, max_length=50, null=True, verbose_name='Apellido Materno')),
                ('ocupacion', models.CharField(max_length=100, verbose_name='Ocupación')),
                ('fotografia', models.ImageField(max_length=200, upload_to='tutor/', verbose_name='Fotografía del Tutor(a)')),
                ('zona', models.CharField(max_length=50, verbose_name='Zona')),
                ('calleavenida', models.CharField(max_length=50, verbose_name='Calle /Avenida')),
                ('numero', models.CharField(blank=True, max_length=50, null=True, verbose_name='Número')),
                ('celular', models.IntegerField(default=0, verbose_name='Nro. Celular')),
                ('expedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='persona.departamento')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='persona.genero')),
                ('tipotutor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='persona.tipotutor')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_eliminacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tutor',
                'verbose_name_plural': 'Tutores',
            },
        ),
    ]
