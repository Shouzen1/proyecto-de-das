from django.urls import path
from  . import views

app_name = 'alumnos'

urlpatterns = [
    path('index', views.index, name='index'),
    path('account', views.account, name='account'),
    path('carrito', views.carrito, name='carrito'),
    path('htedgnf', views.htedgnf, name='htedgnf'),
    path('frida', views.frida, name='frida'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('miguel', views.miguel, name='miguel'),
    path('vincent', views.vincent, name='vincent'),
    path('añadir/', views.añadir_arte, name='añadir_arte'),
    path('listar/', views.listar_arte, name='listar_arte'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.register, name='registro'),
]
