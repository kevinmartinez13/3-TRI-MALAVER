from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    codigo = models.CharField(max_length=10, unique=True, help_text="Ej: MAT, HIS")
    def __str__(self): return self.nombre