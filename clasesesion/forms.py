from django import forms
from .models import ClaseSesion

class ClaseSesionForm(forms.ModelForm):
    class Meta:
        model = ClaseSesion
        fields = ['curso', 'semestre', 'profesor', 'aula', 'horario_texto']

