from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombres = models.CharField(max_length=20, help_text='Nombres del estudiante')
    paterno = models.CharField(max_length=15, help_text='apellido paterno')
    materno = models.CharField(max_length=15, help_text='apellido materno')
    ru = models.CharField(max_length=10, unique=True, help_text='RU del estudiante')
    email = models.EmailField(max_length=190, unique=True, help_text='Correo electronico del estudiante')
    ci = models.CharField(max_length=12, unique=True, help_text='Cedula de identidad del estudiante')

    def __str__(self):
        return self.nombres + ' ' + self.paterno + ' ' + self.materno

    class Meta:
        ordering = ['-paterno', 'materno', 'nombres'] 


class Asignatura (models.Model):
    nombreasic = models.CharField(max_length=30, help_text='Nombre de la asignatura')
    sigla = models.CharField(max_length=6, help_text='Sigla de la asignatura')
    horas = models.IntegerField(help_text='Horas de la asignatura')
    semestre = models.IntegerField(help_text='Semestre de la asignatura')

    def __str__(self):
        return self.sigla

    class Meta:
        ordering = ['nombreasic']

