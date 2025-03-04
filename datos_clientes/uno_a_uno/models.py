from django.db import models

# Create your models here.
class Casa(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=250)
    
    def __str__(self):
        return self.nombre
    
class Propietario(models.Model):
    casa=models.OneToOneField(Casa,on_delete= models.CASCADE,primary_key=True)
    nombre=models.CharField(max_length=50)
    ci=models.CharField(max_length=11)
    celular=models.IntegerField(default=53271799)
    
    def __str__(self):
        return self.casa.nombre