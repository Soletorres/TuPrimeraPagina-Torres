from django.contrib import admin
from .models import Categoria, Autor, Noticia

admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Noticia)