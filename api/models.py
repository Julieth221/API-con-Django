from django.db import models

# Create your models here.
# Aqui se crean los modelos (las tablas o colecciones)

class programmer(models.Model):
    fullname = models.CharField(max_length=50)
    nikname = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField(default=True)
    phone = models.CharField(max_length=10, null=True, default=None)
    is_activate = models.BooleanField(default=True)
    
class student(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)
    num_Ficha = models.PositiveBigIntegerField(default=0)
    formacion = models.BooleanField(default=True)
    fecha_Ingreso = models.DateField()
    
