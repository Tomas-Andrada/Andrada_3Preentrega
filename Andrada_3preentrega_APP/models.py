from django.db import models

# Create your models here.

class Empleados(models.Model):
    nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    correo = models.EmailField()
    telefono = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}-{self.Apellido}"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.nombre}"
    
class Sector(models.Model):
    nombre_sector = models.CharField(max_length=50)
    numero_sector = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.nombre_sector}-{self.numero_sector}"