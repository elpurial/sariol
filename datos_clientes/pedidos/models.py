from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto
from django.db.models import F,Sum,FloatField

# Create your models here.
User=get_user_model()

class Pedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return self.id 
   
   
    @property
    def total(self):
        return self.linea_pedidos_set.aggregate(
            
            total=Sum( F('precio')*('cantidad'),output_field=FloatField())
            
        )["total"] 
    
    class Meta:
      db_table='pedidos'
      verbose_name="pedido"
      verbose_name_plural="pedidos"
      ordering=['id']
      
class LineaPedidos(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido= models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)     
    created= models.DateTimeField(auto_now_add=True,verbose_name="created")
    updated= models.DateTimeField(auto_now_add=True,verbose_name="updated")
    
    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}' 
        

    class Meta:
        db_table='linea_pedidos'
        verbose_name="lineas_Pedidos"
        verbose_name_plural="lineas_Pedidos"
        ordering=['id']
      
      
        