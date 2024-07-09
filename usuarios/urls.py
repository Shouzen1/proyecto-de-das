from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('register/', views.sign_up, name='register'),
    path('logout/', views.sign_out, name='logout'),
    path('home/', views.Home, name='home'),
]
