# Generated by Django 4.1.2 on 2022-10-30 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parametro', '0001_initial'),
        ('persona', '0007_estudiante_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='especialidad',
            name='usuario_creacion',
        ),
        migrations.RemoveField(
            model_name='especialidad',
            name='usuario_eliminacion',
        ),
        migrations.RemoveField(
            model_name='especialidad',
            name='usuario_modificacion',
        ),
        migrations.RemoveField(
            model_name='genero',
            name='usuario_creacion',
        ),
        migrations.RemoveField(
            model_name='genero',
            name='usuario_eliminacion',
        ),
        migrations.RemoveField(
            model_name='genero',
            name='usuario_modificacion',
        ),
        migrations.RemoveField(
            model_name='tipotutor',
            name='usuario_creacion',
        ),
        migrations.RemoveField(
            model_name='tipotutor',
            name='usuario_eliminacion',
        ),
        migrations.RemoveField(
            model_name='tipotutor',
            name='usuario_modificacion',
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='expedido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='parametro.departamento'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='parametro.genero'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='especialidad',
            field=models.ManyToManyField(to='parametro.especialidad'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='expedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='parametro.departamento'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='parametro.genero'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='expedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='parametro.departamento'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='parametro.genero'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='tipotutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='parametro.tipotutor'),
        ),
        migrations.DeleteModel(
            name='Departamento',
        ),
        migrations.DeleteModel(
            name='Especialidad',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
        migrations.DeleteModel(
            name='Tipotutor',
        ),
    ]