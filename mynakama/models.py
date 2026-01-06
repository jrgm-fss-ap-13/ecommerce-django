from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from autoslug import AutoSlugField


# Create your models here.

class Anime(models.Model):
    id_anime = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='nombre', default='')

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'anime'

    
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='nombre_producto')
    stock = models.IntegerField(default=0)
    image1 = models.CharField(max_length=200,null=True,default='-')
    image2 = models.CharField(max_length=200,null=True,default='-')
    image3 = models.CharField(max_length=200,null=True,default='-')
    image4 = models.CharField(max_length=200,null=True,default='-')
    descripcion = models.TextField(null=True)
    precio = models.IntegerField(default=0)
    precio_descuento = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    destacado = models.BooleanField(default=False)
    anime_id_anime = models.ForeignKey(Anime, on_delete=models.CASCADE, db_column='anime_id_anime', default=1000)
  
    def __str__(self):
        return self.nombre_producto

    class Meta:
        db_table = 'producto'

class Manga(Producto):
    editorial = models.CharField(max_length=100,null=True)
    autor = models.CharField(max_length=100,null=True)
    tomo = models.IntegerField(null=True)

    class Meta:
        db_table = 'manga'

class Figura(Producto):
    material = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100, default='Sin fabricante')
    medidas = models.CharField(max_length=100, default=0)
    personaje = models.CharField(max_length=100,null=True)
    
    class Meta:
        db_table = 'figura'


class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    auth_user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='auth_user_id')
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
    )
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')

    def __str__(self):
        return str(self.id_orden) + ' - ' + self.auth_user_id.username
    
    @property
    def get_cart_total(self):
        ordenitems = self.carrito_set.all()
        total = sum([articulo.get_total for articulo in ordenitems ])
        return total
    
    @property
    def get_cart_items(self):
        ordenitems = self.carrito_set.all()
        total = sum([articulo.cantidad for articulo in ordenitems ])
        return total

    class Meta:
        db_table = 'orden'


class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key=True)
    cantidad = models.PositiveIntegerField(default=1)
    producto_id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE , db_column='producto_id_producto')
    orden_id_orden = models.ForeignKey(Orden, on_delete=models.CASCADE, db_column='orden_id_orden',null=True)
    

    @property
    def get_total(self):
        total = self.producto_id_producto.precio * self.cantidad
        return total

    class Meta:
        db_table = 'carrito'

class DetalleVenta(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    orden_id_orden = models.ForeignKey(Orden, on_delete=models.CASCADE, db_column='orden_id_orden',null=True)   
    username = models.CharField(max_length=255)
    total_venta = models.IntegerField(null=True)

    class Meta:
        db_table = 'detalle_venta'

class Empresa(models.Model):
    text1 = models.TextField(null=True)
    text2 = models.TextField(null=True)
    text3 = models.TextField(null=True)
    text4 = models.TextField(null=True)
    image1 = models.CharField(max_length=200 , default= '-')
    nombre_tienda = models.CharField(max_length=200 , default= '-')
    direccion = models.CharField(max_length=200 , default= '-')
    image2 = models.CharField(max_length=200 , default= '-')
    telefono = models.CharField(max_length=200 , default= '-')

    class Meta:
        db_table = 'empresa'