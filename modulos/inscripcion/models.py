from django.db import models
from modulos.logmodel.models import LogModel
from modulos.persona.models import Estudiante
from modulos.curso.models import Curso
from modulos.parametro.models import (
    Documento,
    TipoEstudiante,
)


class Inscripcion(LogModel):
    tipoestudiante = models.ForeignKey(TipoEstudiante, related_name='+', on_delete=models.PROTECT)
    estudiante = models.ForeignKey(Estudiante, related_name='+', on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, related_name='+', on_delete=models.PROTECT)
    gestion = models.IntegerField('Gestión',)
    tipodocumento = models.ManyToManyField(Documento)

    class Meta:
        verbose_name = 'Inscripcion'
        verbose_name_plural = 'Inscripciones'

    def __str__(self):
        return '{0}{1}{2}{3}{4}'.format(self.tipoestudiante, self.estudiante, self.curso,
                                        self.gestion, self.tipodocumento)
