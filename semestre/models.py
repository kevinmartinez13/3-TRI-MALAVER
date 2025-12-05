from django.db import models

class Semestre(models.Model):
    nombre = models.CharField(max_length=50, help_text="Ej: Otoño 2023")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=False)
    def __str__(self): return self.nombre