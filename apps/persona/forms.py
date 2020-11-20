from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput

from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('dni','nombre_completo','fecha_nacimiento','sexo','domicilio')
        widgets = {
            'fecha_nacimiento': DateInput(format='%y-%m-%d', attrs={'type': 'date'})
        }