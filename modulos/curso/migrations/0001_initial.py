# Generated by Django 4.1.2 on 2022-10-30 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parametro', '0005_tipoindicador_indicador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_eliminacion', models.DateTimeField(blank=True, null=True)),
                ('denominacion', models.CharField(max_length=100, verbose_name='Denominación del Curso')),
                ('paralelo', models.CharField(max_length=100, verbose_name='Paralelo')),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='parametro.nivel')),
                ('turno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='parametro.turno')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_eliminacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='MateriaHorario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_eliminacion', models.DateTimeField(blank=True, null=True)),
                ('desde', models.TimeField(verbose_name='Hora Desde')),
                ('hasta', models.TimeField(verbose_name='Hora Hasta')),
                ('gestion', models.IntegerField(verbose_name='Gestión')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='curso.curso')),
                ('dia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='parametro.dia')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='parametro.materia')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_eliminacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Materia y Horario',
                'verbose_name_plural': 'Materias y Horarios',
            },
        ),
    ]
