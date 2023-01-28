from django.db import models
from modulos.logmodel.models import LogModel
from modulos.parametro.models import Indicador
from modulos.persona.models import (
    Estudiante,
    Profesor
)
from modulos.curso.models import Materia


class Asistencia(LogModel):
    estudiante = models.ForeignKey(Estudiante, related_name='+', on_delete=models.PROTECT)
    fecha = models.DateField('Fecha de Asistencia', null=False, blank=False)
    hora_llegada = models.TimeField('Hora de Llegada', null=False, blank=False)
    hora_salida = models.TimeField('Hora de Salida', null=False, blank=False)

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'

    def __str__(self):
        return '{0}{1}{2}{3}'.format(self.estudiante, self.fecha,
                                     self.hora_llegada, self.hora_salida)


class AsistenciaDetalle(LogModel):
    asistencia = models.ForeignKey(Asistencia, related_name='+', on_delete=models.PROTECT)
    profesor = models.ForeignKey(Profesor, related_name='+', on_delete=models.PROTECT)
    materia = models.ForeignKey(Materia, related_name='+', on_delete=models.PROTECT)
    indicador_positivo = models.ForeignKey(Indicador, related_name='+', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Asistencia con Detalle'
        verbose_name_plural = 'Asistencias con Detalles'


class DetalleIndicadoresNegativos(LogModel):
    asistenciadetalle = models.ForeignKey(AsistenciaDetalle, related_name='+', on_delete=models.PROTECT)
    indicador_negativo = models.ForeignKey(Indicador, related_name='+', on_delete=models.PROTECT)
    observacion = models.TextField('Observación', null=True, blank=True)

    class Meta:
        verbose_name = 'Asistencia con Detalle e Indicador negativo'
        verbose_name_plural = 'Asistencias con Detalles e Indicadores negativos'


class AsistenciaIndicadoresNegativosGral(LogModel):
    asistencia = models.ForeignKey(Asistencia, related_name='+', on_delete=models.PROTECT)
    indicador_negativo = models.ForeignKey(Indicador, related_name='+', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Asistencia con Indicador Negativo General'
        verbose_name_plural = 'Asistencias con Indicadores Negativos Generales'
