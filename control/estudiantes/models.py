from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    ciclo = models.CharField(max_length=10)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
