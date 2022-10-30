from django.db import models
from modulos.logmodel.models import LogModel


class Tipotutor(LogModel):
    tutor = models.CharField('Tipo Tutor', max_length=20, null=False, blank=False, unique=True)
    descripcion = models.CharField('Descripción del Tipo', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Tipo de Tutor'
        verbose_name_plural = 'Tipos de Tutores'

    def __str__(self):
        return self.tutor


class Especialidad(LogModel):
    especialidad = models.CharField('Especialidad', max_length=50, null=False, blank=False, unique=True)
    descripcion = models.CharField('Descripción de la Especialidad', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.especialidad


class Genero(LogModel):
    genero = models.CharField('Genero', max_length=10, unique=True, null=False, blank=False)

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

    def __str__(self):
        return self.genero


class Departamento(LogModel):
    sigla = models.CharField('Sigla', max_length=10, unique=True, null=False, blank=False)
    departamento = models.CharField('Departamento', max_length=20, null=False, blank=False)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return '({0}) {1}'.format(self.sigla, self.departamento)


class Documento(LogModel):
    documento = models.CharField('Tipo de Documento', max_length=50, unique=True, null=False, blank=False)
    descripcion = models.CharField('Descripción del Documento', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def __str__(self):
        return self.documento


class Nivel(LogModel):
    nivel = models.CharField('Nivel', max_length=15, unique=True, null=False, blank=False)

    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveles'

    def __str__(self):
        return self.nivel


class Turno(LogModel):
    turno = models.CharField('Turno', max_length=15, unique=True, null=False, blank=False)

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'

    def __str__(self):
        return self.turno


class Materia(LogModel):
    codigo = models.CharField('Cod. Materia', max_length=10, null=False, blank=False)
    denominacion = models.CharField('Denominación Materia', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

    def __str__(self):
        return '{0} {1}'.format(self.codigo, self.denominacion)


class Dia(LogModel):
    sigla = models.CharField('Cod. Dia', max_length=10, null=False, blank=False)
    dia = models.CharField('Denominación del Día', max_length=10, null=False, blank=False)

    class Meta:
        verbose_name = 'Día de la Semana'
        verbose_name_plural = 'Días de la Semana'

    def __str__(self):
        return self.dia


class TipoIndicador(LogModel):
    tipoindicador = models.CharField('Tipo de indicador', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Tipo de Indicador'
        verbose_name_plural = 'Tipos de Indicadores'

    def __str__(self):
        return self.tipoindicador


class Indicador(LogModel):
    denominacion = models.CharField('Indicador', max_length=50, null=False, blank=False)
    valor = models.CharField('Valor del Indicador', max_length=5, null=False, blank=False)
    tipoindicador = models.ForeignKey(TipoIndicador, related_name='+', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Indicador'
        verbose_name_plural = 'Indicadores'

    def __str__(self):
        return '({0}) {1}'.format(self.valor, self.denominacion)


class TipoEstudiante(LogModel):
    tipoestudiante = models.CharField('Tipo de Estudiante', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Tipo de Estudiante'
        verbose_name_plural = 'Tipos de Estudiantes'

    def __str__(self):
        return self.tipoestudiante
