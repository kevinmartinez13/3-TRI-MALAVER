from django.db import models

class Matricula(models.Model):
    estudiante = models.ForeignKey('estudiante.Estudiante', on_delete=models.CASCADE)
    clase_sesion = models.ForeignKey('clasesesion.ClaseSesion', on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('estudiante', 'clase_sesion')
        verbose_name = "Matrícula"

    def __str__(self):
        return f"Matrícula de {self.estudiante_id}"