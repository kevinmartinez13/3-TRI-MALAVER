from django import forms
from .models import Edificio

class EdificioForm(forms.ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion']