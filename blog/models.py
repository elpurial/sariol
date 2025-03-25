from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorias(models.Model):
   nombre = models.CharField(max_length=50,verbose_name="nombre")
   created= models.DateTimeField(auto_now_add=True,verbose_name="created")
   updated= models.DateTimeField(auto_now_add=True,verbose_name="updated")
 
   class Meta:
      verbose_name="categoria"
      verbose_name_plural="categorias"
      
   def __str__(self):
      return self.nombre
  
class Post(models.Model):
   titulo = models.CharField(max_length=50,verbose_name="nombre")
   contenido = models.CharField(max_length=250,verbose_name="contenido")
   imagen = models.ImageField(upload_to="blog",null=True, blank=True)
   autor= models.ForeignKey(User,on_delete= models.CASCADE)#al eliminar elimina todos los post de ese usuario
   categorias=models.ManyToManyField(Categorias)#relacion de varios a varios 
   created= models.DateTimeField(auto_now_add=True,verbose_name="created")
   updated= models.DateTimeField(auto_now_add=True,verbose_name="updated")
 
   class Meta:
      verbose_name="post"
      verbose_name_plural="posts"
      
   def __str__(self):
      return self.titulo
class Reservas(models.Model):
   fecha= models.DateField(verbose_name="fecha")
   cliente = models.CharField(max_length=250,verbose_name="cliente")
   cant_habit=models.IntegerField()
   email=models.EmailField(unique=True)
   fecha_entrada=models.DateField(verbose_name="fecha_entrada")
   fecha_salida=models.DateField(verbose_name="fecha_salida")
   created= models.DateTimeField(auto_now_add=True,verbose_name="created")
   updated= models.DateTimeField(auto_now_add=True,verbose_name="updated")
   class Meta:
      verbose_name="reserva"
      verbose_name_plural="reservas"
   def __str__(self):
      return self.cliente,self.fecha