from django.db import models

# Create your models here.

class Casa_Rodolfo(models.Model):
    nombre=models.CharField( max_length=50)
    cant_habitaciones=models.IntegerField(default=9, name="cant_habitaciones",blank=True,null=True)    
    
    def __str__(self):
       return self.nombre
    
class Habitaciones(models.Model): 
    
    ocupadas=models.IntegerField(null=True,blank=True)
    disponibles=models.IntegerField(null=True,blank=True)
    fecha=models.DateField()
    disponible=models.IntegerField(null=True,blank=True)
    nombre=models.ForeignKey(Casa_Rodolfo,on_delete=models.CASCADE)   
    
    def __str__(self):
        return  str(self.disponible)#porque es un entero el que queremos 