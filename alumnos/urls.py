#from django.conf.urls import url
from django.urls import path
from  . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('crud', views.crud, name='crud'),
    path('alumnosAdd', views.alumnosAdd, name='alumnosAdd'),
]

