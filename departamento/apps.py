from django.contrib import admin
from .models import Departamento
admin.site.register(Departamento)


class DepartamentoConfig(AppConfig):
    name = 'departamento'
