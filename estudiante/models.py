
from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    matricula_id = models.CharField(max_length=20, unique=True, help_text="ID del alumno")
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    def __str__(self): return f"[{self.matricula_id}] {self.apellido}, {self.nombre}"