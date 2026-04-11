from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('noticia/<int:pk>/', views.detalle_noticia, name='detalle_noticia'),
    path('nueva-categoria/', views.nueva_categoria, name='nueva_categoria'),
    path('nuevo-autor/', views.nuevo_autor, name='nuevo_autor'),
    path('nueva-noticia/', views.nueva_noticia, name='nueva_noticia'),
    path('editar-noticia/<int:pk>/', views.EditarNoticia.as_view(), name='editar_noticia'),
    path('borrar-noticia/<int:pk>/', views.BorrarNoticia.as_view(), name='borrar_noticia'),
    path('buscar/', views.buscar, name='buscar'),
]