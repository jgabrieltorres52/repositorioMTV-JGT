from django.db import models

# Create your models here.
class Padres(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    nacimiento = models.DateField()
    email = models.EmailField()
    

class Hermanos(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    nacimiento = models.DateField()
    email = models.EmailField()

class Hijos(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    nacimiento = models.DateField()
    email = models.EmailField()