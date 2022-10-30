# Generated by Django 4.1.2 on 2022-10-30 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_estudiante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='calleavenida',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='numero',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='tipotutor',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='zona',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='tutor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='persona.tutor'),
            preserve_default=False,
        ),
    ]
