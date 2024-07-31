from django.db import models

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    descripcion = models.TextField()
    edad = models.PositiveBigIntegerField()
    
    
    def __str__(self):
        return self.nombre
    
    
class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre    