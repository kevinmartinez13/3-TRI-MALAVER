from django.db import models

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField(blank=True)
    creditos = models.PositiveIntegerField(default=3)
    departamento = models.ForeignKey('departamento.Departamento', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.codigo}: {self.titulo}"
