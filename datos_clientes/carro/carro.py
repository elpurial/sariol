class Carro:
    def __init__(self, request):#el constructor de la clase pra luego utilizarlo 
        self.request = request
        self.session = request.session 
        carro=self.session.get("carro")
        if not carro:
           carro= self.session["carro"]={} #creando un carro que va a tener un diccionario vacio
        self.carro= carro #si el carro existe pues trabajamos con el
        
        
    def agregar(self,producto): #funcion para agregar productos al carro
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id]={
               "producto_id":producto.id,
               "nombre":producto.nombre,
               "precio":str(producto.precio),
               "cantidad":1,
               "imagen":producto.imagen.url
                
            }
        else:# Si el producto existe vamos a incrementarlo
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"]) + producto.precio
                    break 
        self.guardar_carro()        
                
    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True
    
    def eliminar(self,producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    
    def restar_producto(self,producto):
        for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]-1
                    value["precio"]=float(value["precio"])-producto.precio
                    if value["cantidad"] < 1:
                        self.eliminar(producto)  
                    break  
        self.guardar_carro() 
        
    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True
        
                   