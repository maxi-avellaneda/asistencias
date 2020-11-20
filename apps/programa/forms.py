from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput
from datetime import date
from datetime import datetime

from .models import Programa, AsignacionBeneficio,TipoAsistencia


class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ('nombre', 'tipo_asistencias', 'requisitos', 'fecha_inicio', 'fecha_fin')

        widgets = {
            'requisitos': forms.ClearableFileInput(),
            'fecha_inicio': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'fecha_fin': DateInput(format='%y-%m-%d', attrs={'type': 'date'})
        }

    def clean_requisitos(self):
        requisitos = self.cleaned_data['requisitos']
        if requisitos:
            extension = requisitos.name.rsplit('.', 1)[1].lower()
            if extension != 'pdf':
                raise ValidationError('El archivo seleccionado no tiene el formato PDF.')
        return requisitos

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = self.cleaned_data['fecha_inicio']
        fecha_fin = self.cleaned_data['fecha_fin']
        # Verifica que la fecha de inicio sea anterior a fecha fin.
        if fecha_fin and fecha_inicio > fecha_fin:
            raise ValidationError(
                {'fecha_inicio': 'La Fecha de Inicio no puede ser posterior que la fecha fin'},
                code='invalido'
            )
        return cleaned_data


class AsignacionBeneficioForm(forms.ModelForm):
    class Meta:
        model = AsignacionBeneficio
        fields = ('programa','persona','tipo_asistencia','fecha_entrega','cantidad')
        widgets = {
            'fecha_entrega': DateInput(format='%y-%m-%d', attrs={'type': 'date'})
        }
    def clean(self):
        cleaned_data = super().clean()
        cantidad = self.cleaned_data['cantidad']
        fecha_entrega = self.cleaned_data['fecha_entrega']
        ahora = datetime.now()
        if cantidad  < 1:
            raise ValidationError(
                {'cantidad': 'Ingrese una cantidad mayor a 1'},
                code='invalido'
            )
        """
        if fecha_entrega>ahora:
            raise ValidationError(
                {'fecha_entrega': 'Fecha ingresada no puede ser anterior a la fecha actual'},
                code='invalido'
            )
        """
        return cleaned_data

class tipoAsistenciaForm(forms.ModelForm):
    class Meta:
        model = TipoAsistencia
        fields = ('descripcion',)

