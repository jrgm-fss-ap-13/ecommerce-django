from django.shortcuts import render,redirect
from .models import Producto,Figura,Manga,Carrito,Orden,User,DetalleVenta,Anime,Empresa
from django.contrib.auth.decorators import user_passes_test
import random
from django.db import models
from .forms import UserRegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .ProductForm import ProductForm, MangaForm, FiguraForm
# Create your views here.


def index(request):
    if request.user.is_authenticated:   # Verificamos si el usuario está logeado
        usuario = request.user
        orden = Orden.objects.filter(auth_user_id=usuario,estado = 'pendiente').first()  # Filtramos la orden por el usuario y por el estado de la orden
        articulos = orden.carrito_set.all() if orden else []
        items_cantidad_carrito = orden.get_cart_items if orden else 0
    else:
        articulos = []
        orden = {'get_cart_items': 0, 'get_cart_total': 0}
        items_cantidad_carrito = orden['get_cart_items']

    max_id_anime = Anime.objects.aggregate(max_id=models.Max('id_anime'))['max_id']
    max_id_anime = min(max_id_anime, 14)
    random_id = random.randint(1, max_id_anime)

    productos_random = Producto.objects.filter(anime_id_anime=random_id, activo=True)
    anime_nombre = Anime.objects.get(id_anime=random_id)

    productos_destacados = Producto.objects.filter(activo=True, destacado = True)
    anime_destacados = 'Destacados'

    productos_kimetsu = Producto.objects.filter(activo=True, anime_id_anime = 3)
    kimetsu_nombre = Anime.objects.get(id_anime = 3)

    #productos = Producto.objects.filter(activo=True)
    context = {'articulos': articulos,
            'orden': orden,
            'items_cantidad_carrito': items_cantidad_carrito,
            'productos_kimetsu' : productos_kimetsu,
            'nombre_anime_kimetsu': kimetsu_nombre.nombre,
            'productos_random':productos_random,
            'anime_nombre': anime_nombre,
            'productos_destacados': productos_destacados,
            'anime_destacados': anime_destacados }
    return render(request, 'index.html', context)


def info_producto(request, slug):
    if request.user.is_authenticated:   # Verificamos si el usuario está logeado
        usuario = request.user
        orden = Orden.objects.filter(auth_user_id=usuario,estado = 'pendiente').first()  # Filtramos la orden por el usuario y por el estado de la orden
        articulos = orden.carrito_set.filter(producto_id_producto__slug=slug) if orden else []
        items_cantidad_carrito = orden.get_cart_items if orden else 0
    else:
        articulos = []
        orden = {'get_cart_items': 0, 'get_cart_total': 0}
        items_cantidad_carrito = orden['get_cart_items']
    productos = Producto.objects.filter(slug=slug)
    print(productos)
    return render(request, 'info_productos.html', {'productos': productos,'articulos': articulos,'items_cantidad_carrito': items_cantidad_carrito})


def productos_filtrados(request, subclase, anime_slug=None):
    if request.user.is_authenticated:   # Verificamos si el usuario está logeado
        usuario = request.user
        orden = Orden.objects.filter(auth_user_id=usuario,estado = 'pendiente').first()  # Filtramos la orden por el usuario y por el estado de la orden
        articulos = orden.carrito_set.all() if orden else []
        items_cantidad_carrito = orden.get_cart_items if orden else 0
    else:
        articulos = []
        orden = {'get_cart_items': 0, 'get_cart_total': 0}
        items_cantidad_carrito = orden['get_cart_items']
    
    if subclase == 'figuras':
        if anime_slug:
            anime = Anime.objects.get(slug=anime_slug)
            productos = Figura.objects.filter(anime_id_anime=anime,activo=True)
        else:
            productos = Figura.objects.filter(activo=True)
    elif subclase == 'mangas':
        if anime_slug:
            anime = Anime.objects.get(slug=anime_slug)
            productos = Manga.objects.filter(anime_id_anime=anime,activo=True)
        else:
            productos = Manga.objects.filter(activo=True)
    else:
        productos = Producto.objects.filter(activo=True)

    ordenamiento = request.GET.get('orderby')
    if ordenamiento == 'ascendente':
        productos = productos.order_by('precio')
    elif ordenamiento == 'descendente':
        productos = productos.order_by('-precio')

    nombre_anime = None
    if anime_slug:
        nombre_anime = Anime.objects.get(slug=anime_slug).nombre

    context = {
        'productos': productos,
        'subclase': subclase,
        'articulos': articulos,
        'items_cantidad_carrito': items_cantidad_carrito,
        'anime_slug': anime_slug,
        'nombre_anime': nombre_anime,
        
    }
    return render(request, 'productos_filtrados.html', context)


def carrito(request):
    if request.user.is_authenticated:   # Verificamos si el usuario está logeado
        usuario = request.user
        orden = Orden.objects.filter(auth_user_id=usuario,estado = 'pendiente').first()  # Filtramos la orden por el usuario y por el estado de la orden
        articulos = orden.carrito_set.all() if orden else []
        items_cantidad_carrito = orden.get_cart_items if orden else 0
    else:
        articulos = []
        orden = {'get_cart_items': 0, 'get_cart_total': 0}
        items_cantidad_carrito = orden['get_cart_items']    
    return render(request, 'cart.html', {'orden': orden,'articulos':articulos, 'items_cantidad_carrito': items_cantidad_carrito})

@login_required
def agregar_al_carrito(request, producto_id):
    usuario = request.user
    orden, created = Orden.objects.get_or_create(auth_user_id=usuario,estado = 'pendiente')
    print(created)
    producto = Producto.objects.get(id_producto=producto_id)
    
    # Verificar si el producto ya está en el carrito
    carrito_existente = Carrito.objects.filter(orden_id_orden=orden, producto_id_producto=producto).exists()
    if carrito_existente:
        # Si el producto ya está en el carrito, puedes manejarlo según tus necesidades
        # Por ejemplo, aumentar la cantidad en lugar de crear un nuevo objeto Carrito
        carrito = Carrito.objects.get(orden_id_orden=orden, producto_id_producto=producto)
        carrito.cantidad += 1
        carrito.save()
    else:
        # Si el producto no está en el carrito, crea un nuevo objeto Carrito y guárdalo en la base de datos
        carrito = Carrito(orden_id_orden=orden, producto_id_producto=producto)
        carrito.save()
    
    return redirect(request.META['HTTP_REFERER'])

def eliminar_producto(request, producto_id):
    # Obtén el producto a eliminar del carrito
    producto = Producto.objects.get(id_producto=producto_id)

    # Elimina el producto del carrito
    usuario = request.user
    orden = Orden.objects.filter(auth_user_id=usuario, estado='pendiente').first()
    carrito = Carrito.objects.filter(orden_id_orden=orden, producto_id_producto=producto)
    carrito.delete()

    return redirect('carrito')

def vaciar_carrito(request):
    # Obtén el usuario actual
    usuario = request.user

    # Obtén la orden pendiente del usuario
    orden = Orden.objects.filter(auth_user_id=usuario, estado='pendiente').first()

    # Elimina todos los productos del carrito asociados a la orden
    carrito = Carrito.objects.filter(orden_id_orden=orden)
    carrito.delete()

    return redirect('carrito')

@login_required
def restar_producto(request, producto_id):
    # Obtén el producto a eliminar del carrito
    producto = Producto.objects.get(id_producto=producto_id)
    usuario = request.user

    # Obtén la orden pendiente del usuario
    orden = Orden.objects.filter(auth_user_id=usuario, estado='pendiente').first()

    if orden:
        carrito = Carrito.objects.filter(orden_id_orden=orden, producto_id_producto=producto).first()
        
        if carrito.cantidad > 1:
            carrito.cantidad -= 1
            carrito.save()
        else:
            carrito.delete()

    return redirect(request.META['HTTP_REFERER'])


def finalizar_compra(request):
    # Obtener la orden actual del usuario
    usuario = request.user
    orden = Orden.objects.filter(auth_user_id=usuario, estado='pendiente').first()

    if orden:
        # Cambiar el estado de la orden a 'Completada'
        orden.estado = 'completada'
        orden.save()

        # Restar el stock de los productos en el carrito
        carrito_items = orden.carrito_set.all()

        for item in carrito_items:
            producto = item.producto_id_producto
            cantidad_comprada = item.cantidad
            producto.stock -= cantidad_comprada
            producto.save()

        # Crear un nuevo objeto DetalleVenta y guardarlo en la base de datos
        detalle_venta = DetalleVenta(orden_id_orden=orden, username=usuario.username, total_venta=orden.get_cart_total)
        detalle_venta.save()

        # Resto de la lógica de finalización de la compra
    return redirect('index')


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            # Realizar redireccionamiento o mostrar un mensaje de éxito
    else:
        form = UserRegistrationForm()

    if request.user.is_authenticated:   # Verificamos si el usuario está logeado
        usuario = request.user
        orden = Orden.objects.filter(auth_user_id=usuario,estado = 'pendiente').first()  # Filtramos la orden por el usuario y por el estado de la orden
        articulos = orden.carrito_set.all() if orden else []
        items_cantidad_carrito = orden.get_cart_items if orden else 0
    else:
        articulos = []
        orden = {'get_cart_items': 0, 'get_cart_total': 0}
        items_cantidad_carrito = orden['get_cart_items']

    return render(request, 'register.html', {'form': form,'items_cantidad_carrito': items_cantidad_carrito,})


def LoginView(request):

    return render(request,'login.html',{})


def info_nakama(request):

    empresa = Empresa.objects.all() 
    context = {'empresa' : empresa}

    return render(request, 'info_nakama.html', context  )


def adm_productos(request):
    
    ordenamiento = request.GET.get('orderby')
    ordenamiento_stock = request.GET.get('orderbystock')
    anime_id = request.GET.get('anime')

    productos = Producto.objects.filter(activo=True)
    animes = Anime.objects.all()

    if anime_id:
        productos = productos.filter(anime_id_anime=anime_id)

    if ordenamiento == 'ascendente':
        productos = productos.order_by('precio')
    elif ordenamiento == 'descendente':
        productos = productos.order_by('-precio')

    if ordenamiento_stock == 'ascendente':
        productos = productos.order_by('stock')
    elif ordenamiento_stock == 'descendente':
        productos = productos.order_by('-stock')

    context = {'productos' : productos, 'animes' : animes}
    return render(request, 'panel_administrador.html',context)

def cambiar_estado_producto(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    producto.activo = False
    producto.save()
    return redirect('panel_administrador')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            # Realizar acciones adicionales, como redireccionar a otra página
    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'panel_administrador.html', context)