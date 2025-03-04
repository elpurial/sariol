from django.db import models


# Create your models here.
class Reserva(models.Model):
    fecha= models.DateField(auto_now_add=True)
    fecha_entrada=models.DateField()
    fecha_salida=models.DateField()
    cant_habitaciones=models.IntegerField()
    cant_personas=models.IntegerField()
    
    def __str__(self):
        return self.fecha
    
    
class Cliente(models.Model):
    nombre=models.CharField(max_length=50,blank=False,null=False)
    pasaporte=models.CharField(max_length=10,blank=False,null=False)
    mail=models.EmailField(blank=False,null=False)
    pais=models.CharField(max_length=50,blank=False,null=False)
    
    def __str__(self):
        return self.nombre

class Disponible(models.Model):
    fecha= models.DateField()
    habitaciones=models.IntegerField()  