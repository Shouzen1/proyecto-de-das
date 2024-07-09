from django.urls import path

from . import views

urlpatterns = [
    path('crud_artista', views.crud_artista, name='crud_artista'),
    path('carrito/', views.carrito_view, name='carrito'),
    path('agregar_al_carrito/<int:obra_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/clear/', views.clear_cart, name='clear_cart'),
    path('carrito/remove/', views.remove_from_cart, name='remove_from_cart'),
    path('añadir_direccion/', views.añadir_direccion, name='añadir_direccion'),
    path('home/', views.Home, name='home'),
]