from django.db import models


# Create your models here.
class calificacion (models.Model):
    parcial1 = models.IntegerField(help_text='Primer parcial')
    parcial2 = models.IntegerField(help_text='Segundo parcial')
    parcial3 = models.IntegerField(help_text='Tercer parcial')
    practica = models.IntegerField(help_text='Practica')
    laboratorio = models.IntegerField(help_text='Laboratorio')
    final = models.IntegerField(help_text='Final')

    def __str__(self):
        return self.parcial1 + ' ' + self.parcial2 + ' ' + self.parcial3 + ' ' + self.practica + ' ' + self.laboratorio + ' ' + self.final

    class Meta:
        ordering = ['parcial1', 'parcial2', 'parcial3', 'practica', 'laboratorio', 'final']
