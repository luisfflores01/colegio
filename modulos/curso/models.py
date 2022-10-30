from django.db import models
from modulos.logmodel.models import LogModel
from modulos.parametro.models import (
    Nivel,
    Turno,
    Materia,
    Dia,
)
from modulos.persona.models import Profesor


class Curso(LogModel):
    denominacion = models.CharField('Denominación del Curso', max_length=100, null=False, blank=False)
    paralelo = models.CharField('Paralelo', max_length=100)
    nivel = models.ForeignKey(Nivel, related_name='+', on_delete=models.PROTECT)
    turno = models.ForeignKey(Turno, related_name='+', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return '{0}({1}) NIVEL: {2}, TURNO: {3}'.format(self.denominacion, self.paralelo, self.nivel, self.turno)


class MateriaHorario(LogModel):
    curso = models.ForeignKey(Curso, related_name='+', on_delete=models.PROTECT)
    materia = models.ForeignKey(Materia, related_name='+', on_delete=models.PROTECT)
    desde = models.TimeField('Hora Desde', null=False, blank=False)
    hasta = models.TimeField('Hora Hasta', null=False, blank=False)
    dia = models.ForeignKey(Dia, related_name='+', on_delete=models.PROTECT)
    gestion = models.IntegerField('Gestión',)
    profesor = models.ForeignKey(Profesor, related_name='+', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Materia y Horario'
        verbose_name_plural = 'Materias y Horarios'

    def __str__(self):
        return '{0} {1} {2} {3} {4} ({5}) {6}'.format(self.curso, self.profesor, self.materia, self.desde, self.hasta,
                                                      self.dia, self.gestion)
