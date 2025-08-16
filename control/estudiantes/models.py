from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    ciclo = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return self.nombre