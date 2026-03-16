from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nueva-categoria/', views.nueva_categoria, name='nueva_categoria'),
    path('nuevo-autor/', views.nuevo_autor, name='nuevo_autor'),
    path('nueva-noticia/', views.nueva_noticia, name='nueva_noticia'),
    path('buscar/', views.buscar, name='buscar'),
]