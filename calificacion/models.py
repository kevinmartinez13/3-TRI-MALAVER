from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Calificacion(models.Model):
    matricula = models.OneToOneField('matricula.Matricula', on_delete=models.CASCADE)
    valor = models.DecimalField(
        max_digits=4, 
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(10.00)],
        help_text="Calificación de 0.00 a 10.00"
    )
    comentarios = models.TextField(blank=True)

    class Meta:
        verbose_name = "Calificación Final"
        verbose_name_plural = "Calificaciones Finales"

    def __str__(self): return f"Nota: {self.valor}"