from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

urlpatterns = [
    # Urls del index
    path('', views.index , name='index'),
    path('info_nakama', views.info_nakama,name ='info_nakama'),
    #Urls del Producto
    path('producto/<slug:slug>/',views.info_producto,name='info-producto'),
    path('productos/<str:subclase>/',views.productos_filtrados , name='productos_filtrados'),
    path('productos/<str:subclase>/<str:anime_slug>/', views.productos_filtrados, name='productos_filtrados_anime'),
    #Urls del Carrito y funcionalidades
    path('carrito/', views.carrito ,name='carrito'),
    path('agregar-al-carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('restar_producto/<int:producto_id>/', views.restar_producto, name='restar_producto'),
    path('finalizar-compra/', views.finalizar_compra, name='finalizar_compra'),
    path('vaciar_carrito/', views.vaciar_carrito, name='vaciar_carrito'),
    #Urls del Usuario
    path('register/', views.register_user, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    #Urls del Usuario
    path('panel_administrador/', views.adm_productos, name='panel_administrador'),
    path('cambiar_estado_producto/<int:producto_id>/', views.cambiar_estado_producto, name='cambiar_estado_producto'),
]

