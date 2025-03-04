from django.db import models

# Create your models here.
class Gestor(models.Model):
    nombre = models.CharField(max_length=100)
    # Campo de relación muchos-a-muchos con Usuario
    usuarios = models.ManyToManyField('Usuario', related_name='gestores')

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
