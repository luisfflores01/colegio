from django.db import models
from modulos.logmodel.models import LogModel
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
from .validators import validar_celular
from modulos.parametro.models import (
    Departamento,
    Genero,
    Tipotutor,
    Especialidad
)


class Tutor(LogModel):
    documento = models.CharField('Carnet de Identidad', max_length=15, unique=True, null=False, blank=False)
    expedido = models.ForeignKey(Departamento, related_name='+', on_delete=models.PROTECT)
    nombre = models.CharField('Nombres', max_length=50, null=False, blank=False)
    apellido_paterno = models.CharField('Apellido Paterno', max_length=50, null=True, blank=True)
    apellido_materno = models.CharField('Apellido Materno', max_length=50, null=True, blank=True)
    genero = models.ForeignKey(Genero, related_name='+', on_delete=models.PROTECT)
    ocupacion = models.CharField('Ocupación', max_length=100, null=False, blank=False)
    fotografia = models.ImageField('Fotografía del Tutor(a)', max_length=200, upload_to='media/tutor/',
                                   null=True, blank=True)
    tipotutor = models.ForeignKey(Tipotutor, related_name='+', on_delete=models.PROTECT)
    zona = models.CharField('Zona', max_length=50)
    calleavenida = models.CharField('Calle /Avenida', max_length=50)
    numero = models.CharField('Número', max_length=50, null=True, blank=True)
    celular = models.IntegerField('Nro. Celular', default=0, validators=[validar_celular, ])

    @property
    def imagen_preview(self):
        if self.fotografia:
            _imagen = get_thumbnail(self.fotografia, '200x200', upscale=False, crop=False, quality=100)
            return format_html('<img src="{0}" width="{1}" height="{2}"/>'.format(_imagen.url,
                                                                                  _imagen.width,
                                                                                  _imagen.height))
        return ""

    @property
    def imagen_tag(self):
        if self.fotografia:
            _imagen = get_thumbnail(self.fotografia, '50x50', upscale=False, crop=False, quality=100)
            return format_html('<img src="{0}" width="{1}" height="{2}"/ style="border-radius:50%">'
                               .format(_imagen.url, _imagen.width, _imagen.height))
        return ""

    class Meta:
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'

    def __str__(self):
        return '({0} {1}) {2} {3} {4}'.format(self.documento, self.expedido, self.nombre,
                                              self.apellido_paterno, self.apellido_materno)


class Estudiante(LogModel):
    rude = models.CharField('Nro. Rude', max_length=20, unique=True, null=False, blank=False)
    nombre = models.CharField('Nombres', max_length=50, null=False, blank=False)
    apellido_paterno = models.CharField('Apellido Paterno', max_length=50, null=True, blank=True)
    apellido_materno = models.CharField('Apellido Materno', max_length=50, null=True, blank=True)
    genero = models.ForeignKey(Genero, related_name='+', on_delete=models.PROTECT)
    documento = models.CharField('Carnet de Identidad', max_length=15, null=True, blank=True)
    expedido = models.ForeignKey(Departamento, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', null=False, blank=False)
    fotografia = models.ImageField('Fotografía del Estudiante', max_length=200, upload_to='media/estudiante/',
                                   null=True, blank=True)
    tutor = models.ForeignKey(Tutor, related_name='+', on_delete=models.PROTECT)
    celular = models.IntegerField('Nro. Celular', default=0, validators=[validar_celular, ])

    @property
    def imagen_preview(self):
        if self.fotografia:
            _fotografia = get_thumbnail(self.fotografia, '200x200', upscale=False, crop=False, quality=100)
            return format_html('<img src="{0}" width="{1}" height="{2}">'.format(_fotografia.url,
                                                                                 _fotografia.width,
                                                                                 _fotografia.height))
        return ""

    @property
    def imagen_tag(self):
        if self.fotografia:
            _fotografia = get_thumbnail(self.fotografia, '50x50', upscale=False, crop=False, quality=100)
            return format_html('<img src="{0}" width="{1}" height="{2}"/ style="border-radius:50%">'.
                               format(_fotografia.url, _fotografia.width, _fotografia.height))
        return ""

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return '({0}) {1} {2} {3}'.format(self.rude, self.nombre, self.apellido_paterno, self.apellido_materno)


class Profesor(LogModel):
    documento = models.CharField('Carnet de Identidad', max_length=15, unique=True)
    expedido = models.ForeignKey(Departamento, related_name='+', on_delete=models.PROTECT)
    nombre = models.CharField('Nombres', max_length=50, null=False, blank=False)
    apellido_paterno = models.CharField('Apellido Paterno', max_length=50, null=True, blank=True)
    apellido_materno = models.CharField('Apellido Materno', max_length=50, null=True, blank=True)
    genero = models.ForeignKey(Genero, related_name='+', on_delete=models.PROTECT)
    fotografia = models.ImageField('Fotografía del Profesor(a)', max_length=200, upload_to='media/profesor/',
                                   null=True, blank=True)
    celular = models.IntegerField('Nro. Celular', default=0, validators=[validar_celular, ])
    especialidad = models.ManyToManyField(Especialidad)

    @property
    def imagen_preview(self):
        if self.fotografia:
            _fotografia = get_thumbnail(self.fotografia, '200x200', upscale=False, crop=False, quality=100)
            return format_html('<img src="{0}" width="{1}" height="{2}">'.format(_fotografia.url,
                                                                                 _fotografia.width,
                                                                                 _fotografia.height))
        return ""

    @property
    def imagen_tag(self):
        if self.fotografia:
            _fotografia = get_thumbnail(self.fotografia, '55x55', upscale=False, crop=False, quality=100)
            return format_html('<img src="{0}" width="{1}" height="{2}" / style="border-radius:50%">'
                               .format(_fotografia.url, _fotografia.width, _fotografia.height))
        return ""

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):
        if self.apellido_paterno is None and self.apellido_materno is None:
            return '({0}) {1}'.format(self.documento, self.nombre)
        if self.apellido_materno is None:
            return '({0}) {1} {2}'.format(self.documento, self.nombre, self.apellido_paterno)
        return '({0}) {1} {2} {3}'.format(self.documento, self.nombre, self.apellido_paterno, self.apellido_materno)
