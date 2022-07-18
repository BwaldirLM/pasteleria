from calendar import c
from django.db import models

TAMAÑOS = [
    ('P','PEQUEÑO'), 
    ('M','MEDIANO'),
    ('G','GRANDE')]

# Create your models here.

class Pastel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=50)
    descripcion = models.TextField('Descripcion')
    precio = models.FloatField('Precio')
    tamaño = models.CharField('Tamaño', choices= TAMAÑOS, max_length=10)

    def __str__(self) -> str:
        return self.nombre


class Produccion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha')
    cantidad = models.IntegerField('Cantidad')
    pastel = models.ForeignKey(Pastel, on_delete=models.CASCADE)