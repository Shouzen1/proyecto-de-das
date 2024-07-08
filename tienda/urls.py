from django.urls import path

from . import views

urlpatterns = [
    path('crud_artista', views.crud_artista),
    path('carrito/', views.carrito_view, name='carrito'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('carrito/clear/', views.clear_cart, name='clear_cart'),
    path('carrito/remove/', views.remove_from_cart, name='remove_from_cart'),
]