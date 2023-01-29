from django import forms
from modulos.parametro.models import Indicador
from .models import AsistenciaDetalle


class IndicadorPositivoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['indicador_positivo'].queryset = Indicador.objects.filter(tipoindicador_id=1)


class IndicadorNegativoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['indicador_negativo'].queryset = Indicador.objects.filter(tipoindicador_id=2)

