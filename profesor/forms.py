# profesor/forms.py
from django import forms
from .models import Profesor

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'fecha_contratacion', 'departamento']
        widgets = {
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'})
        }
