from django.db import models
from datetime import date,datetime
from django.utils import timezone

# Create your models here.
class Reserva(models.Model):
    cliente=models.CharField(max_length=50,verbose_name="cliente")
    correo=models.EmailField(max_length=250,verbose_name="correo") 
    cant_habitaciones=models.IntegerField(verbose_name="cant_habitaciones") 
    cant_dias=models.IntegerField(verbose_name="cant_dias") 
    pais=models.CharField(max_length=50,verbose_name="pais")
    cena=models.BooleanField(verbose_name="cena", null=True)
    desayuno=models.BooleanField(verbose_name="desayuno", null=True)
    fecha_entrada=models.DateField(null=True)
    fecha_salida=models.DateField(null=True)
    cant_personas=models.IntegerField(verbose_name="cant_personas")
    comentarios=models.TextField(verbose_name="comentarios")   
    
    def __str__(self):
      return self.cliente
    
    
class Disponibilidad(models.Model):
    fecha=models.DateField(default=date.today)
    disponible=models.IntegerField(verbose_name="disponible")
    cliente=models.ForeignKey(Reserva,on_delete=models.CASCADE)  
    
    
    def __str__(self):
      return self.fecha,self.disponible
    
    