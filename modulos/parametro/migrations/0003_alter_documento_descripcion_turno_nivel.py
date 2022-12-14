# Generated by Django 4.1.2 on 2022-10-30 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parametro', '0002_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Descripción del Documento'),
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_eliminacion', models.DateTimeField(blank=True, null=True)),
                ('turno', models.CharField(max_length=15, unique=True, verbose_name='Turno')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_eliminacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
            },
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_eliminacion', models.DateTimeField(blank=True, null=True)),
                ('nivel', models.CharField(max_length=15, unique=True, verbose_name='Nivel')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_eliminacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Nivel',
                'verbose_name_plural': 'Niveles',
            },
        ),
    ]
