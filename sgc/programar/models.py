from django.db import models

# Create your models here.
class ProgramarM (models.Model):
    gestion = models.CharField(max_length=4, help_text='Gestion del programa')
    grupo = models.CharField(max_length=10,  help_text='Grupo del programa')

    def __str__(self):
        return self.grupo + ' ' + self.gestion

    class Meta:
        ordering = ['-gestion', 'grupo']