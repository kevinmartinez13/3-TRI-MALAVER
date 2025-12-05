from django.db import models

class ClaseSesion(models.Model):
    # Todas son relaciones externas a otras apps
    curso = models.ForeignKey('curso.Curso', on_delete=models.CASCADE, related_name='sesiones')
    semestre = models.ForeignKey('semestre.Semestre', on_delete=models.CASCADE)
    profesor = models.ForeignKey('profesor.Profesor', on_delete=models.SET_NULL, null=True, blank=True)
    aula = models.ForeignKey('aula.Aula', on_delete=models.SET_NULL, null=True, blank=True)

    horario_texto = models.CharField(max_length=100, help_text="Ej: Lunes y Miércoles 10:00-11:30")

    class Meta:
        verbose_name = "Sesión de Clase"
        verbose_name_plural = "Sesiones de Clases"

    def __str__(self):
        return f"{self.curso.codigo if self.curso else 'N/A'} ({self.semestre})"