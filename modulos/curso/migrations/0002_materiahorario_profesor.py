# Generated by Django 4.1.2 on 2022-10-30 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0008_remove_especialidad_usuario_creacion_and_more'),
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiahorario',
            name='profesor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='persona.profesor'),
            preserve_default=False,
        ),
    ]