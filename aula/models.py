from django.db import models

class Aula(models.Model):
    numero = models.CharField(max_length=20)
    edificio = models.ForeignKey('edificio.Edificio', on_delete=models.CASCADE, related_name='aulas')
    capacidad = models.PositiveIntegerField(default=30)
    def __str__(self): return f"Salón {self.numero}"