from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categoria, Autor, Noticia
from .forms import CategoriaForm, AutorForm, NoticiaForm

# Vista home
def home(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/home.html', {'noticias': noticias})

# Vista detalle de noticia
def detalle_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'noticias/detalle_noticia.html', {'noticia': noticia})

# Vista nueva categoria - requiere login
@login_required
def nueva_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CategoriaForm()
    return render(request, 'noticias/formulario_categoria.html', {'form': form})

# Vista nuevo autor - requiere login
@login_required
def nuevo_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AutorForm()
    return render(request, 'noticias/formulario_autor.html', {'form': form})

# Vista nueva noticia - requiere login
@login_required
def nueva_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/formulario_noticia.html', {'form': form})

# Vista buscar
def buscar(request):
    resultados = []
    if request.method == 'GET':
        query = request.GET.get('q', '')
        if query:
            resultados = Noticia.objects.filter(titulo__icontains=query)
    return render(request, 'noticias/buscar.html', {'resultados': resultados})

# CBV - Editar noticia con LoginRequiredMixin
class EditarNoticia(LoginRequiredMixin, UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticias/formulario_noticia.html'
    success_url = reverse_lazy('home')

# CBV - Borrar noticia con LoginRequiredMixin
class BorrarNoticia(LoginRequiredMixin, DeleteView):
    model = Noticia
    template_name = 'noticias/confirmar_borrado.html'
    success_url = reverse_lazy('home')

def about(request):
    return render(request, 'noticias/about.html')