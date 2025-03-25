from django.db import models


# Create your models here.
class Servicios(models.Model):
   nombre = models.CharField(max_length=50,verbose_name="nombre")
   precio = models.FloatField(verbose_name="precio")
   horario= models.CharField(max_length=100,verbose_name="horario")
   imagen = models.ImageField(upload_to="servicios")
   created= models.DateTimeField(auto_now_add=True,verbose_name="created")
   updated= models.DateTimeField(auto_now_add=True,verbose_name="updated")
 
   class Meta:
      verbose_name="servicios"
      verbose_name_plural="servicios"
      
   def __str__(self):
      return self.nombre
