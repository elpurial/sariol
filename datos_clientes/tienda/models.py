from django.db import models

# Create your models here.
class Categoria_producto(models.Model):
   nombre = models.CharField(max_length=50,verbose_name="nombre")
   created= models.DateTimeField(auto_now_add=True,verbose_name="created")
   updated= models.DateTimeField(auto_now_add=True,verbose_name="updated")
 
   class Meta:
      verbose_name="categoria_producto"
      verbose_name_plural="categoria_producto"
      
   def __str__(self):
      return self.nombre

class Producto(models.Model):
   nombre= models.CharField(max_length=50,verbose_name="nombre")
   categoria=models.ForeignKey(Categoria_producto,on_delete=models.CASCADE)
   imagen= models.ImageField(upload_to="tienda",null=True,blank=True)   
   precio= models.FloatField()
   disponibilidad=models.BooleanField(default=True)
   created= models.DateTimeField(auto_now_add=True,verbose_name="created")
   updated= models.DateTimeField(auto_now_add=True,verbose_name="updated")
   

   class Meta:
      verbose_name="producto"
      verbose_name_plural="productos"
      
   def __str__(self):
      return self.nombre