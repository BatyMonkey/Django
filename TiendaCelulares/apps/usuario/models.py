from django.db import models

class Celular(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='static/celulares/')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return str(self.celular)