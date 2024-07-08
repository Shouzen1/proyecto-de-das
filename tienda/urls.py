from django.urls import path

from . import views

urlpatterns = [
    path('crud_artista', views.crud_artista),
]