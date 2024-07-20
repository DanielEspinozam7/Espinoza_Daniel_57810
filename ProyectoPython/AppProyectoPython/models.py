from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=200)
    marca = models.CharField(max_length=50)
    stock = models.IntegerField()
    precio = models.IntegerField()
    url = models.CharField(max_length=200)
    
    #Esta funcion __str__ mostrará en la app admin el string que elijamos como atributo
    def __str__(self):
        return f"{self.nombreProducto}"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}"
    
class FichaProducto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    especificacion = models.TextField()
    
    def __str__(self):
        return f"{self.titulo}"
    
class Cotizacion(models.Model):
    detalle = models.TextField()
    mayorista = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.detalle}, {self.mayorista}"
    
    
    #Con eso se define el nombre en singular y plurar para la entidad
    
    class Meta:
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizaciones'
        #Puedo definir cómo deseo el orden de mis datos en la tabla
        ordering = ["detalle", "mayorista"]
        

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} {self.imagen}"