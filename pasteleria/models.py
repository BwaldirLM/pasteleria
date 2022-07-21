from calendar import c
from django.db import models
from django.contrib.auth.models import AbstractUser

TAMAÑOS = [
    ('P','PEQUEÑO'), 
    ('M','MEDIANO'),
    ('G','GRANDE')]

PAGO = [
    ('Tarjeta', 'TARJETA'),
    ('Efectivo', 'EFECTIVO')
]

# Create your models here.


class User(AbstractUser):
    dni = models.CharField('DNI', max_length=8, unique=True)
    telefono = models.CharField('Telefono', max_length=15)
    direccion = models.TextField('Direccion')

    class Meta:
        db_table = 'auth_user'

class JefeProduccion(models.Model):
    id = models.AutoField(primary_key=True)
    sueldo = models.FloatField('Sueldo')
    descripcion = models.TextField('Descripcion')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, )


class Vendedor(models.Model):
    id = models.AutoField(primary_key=True)
    sueldo = models.FloatField('Sueldo')
    descripcion = models.TextField('Descripcion')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, )



class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado',default=True)
    fecha_registro = models.DateField('Fecha de registro', auto_now_add=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, )



class Pastel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=50)
    descripcion = models.TextField('Descripcion')
    precio = models.FloatField('Precio')
    tamaño = models.CharField('Tamaño', choices= TAMAÑOS, max_length=10)

    class Meta:
        verbose_name = 'Pastel'
        verbose_name_plural = 'Pasteles'

    def __str__(self) -> str:
        return self.nombre


class Produccion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha')
    cantidad = models.IntegerField('Cantidad')
    pastel = models.ForeignKey(Pastel, on_delete=models.CASCADE)

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha', auto_now_add=True)
    importe = models.FloatField('Importe')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    Vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, verbose_name='Vendedor')

class VentaDetalle(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField('Cantidad', default = 1)
    pastel = models.ForeignKey(Pastel, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)

class Pago(models.Model):
    id = models.AutoField(primary_key=True)
    forma_pago = models.CharField('Forma de pago', max_length=8, choices=PAGO)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
