from django.shortcuts import render, redirect
from .models import Categoria, Autor, Noticia
from .forms import CategoriaForm, AutorForm, NoticiaForm

def home(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/home.html', {'noticias': noticias})

def nueva_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CategoriaForm()
    return render(request, 'noticias/formulario_categoria.html', {'form': form})

def nuevo_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AutorForm()
    return render(request, 'noticias/formulario_autor.html', {'form': form})

def nueva_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/formulario_noticia.html', {'form': form})

def buscar(request):
    resultados = []
    if request.method == 'GET':
        query = request.GET.get('q', '')
        if query:
            resultados = Noticia.objects.filter(titulo__icontains=query)
    return render(request, 'noticias/buscar.html', {'resultados': resultados})