from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_contratacion = models.DateField()
    departamento = models.ForeignKey('departamento.Departamento', on_delete=models.SET_NULL, null=True)
    def __str__(self): return f"{self.apellido}, {self.nombre}"