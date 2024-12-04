from django.db import models

# Create your models here.
# Aqui se crean los modelos (las tablas o colecciones)

class programmer(models.Model):
    fullname = models.CharField(max_length=50)
    nikname = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField(default=True)
    phone = models.CharField(max_length=10, null=True, default=None)
    is_activate = models.BooleanField(default=True)
    
