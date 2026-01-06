from django.contrib import admin
from .models import Producto,Carrito,Manga,Figura,Orden,Anime,DetalleVenta,Empresa


# Register your models here.

admin.site.register(Anime)
admin.site.register(Carrito)
admin.site.register(Manga)
admin.site.register(Figura)
admin.site.register(Orden)
admin.site.register(Producto)
admin.site.register(DetalleVenta)
admin.site.register(Empresa)


