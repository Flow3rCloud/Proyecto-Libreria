from django.shortcuts import render
from django.http import HttpResponse

from books.forms import LibroForms


# Create your views here.
def index(request):
    return render(request, 'books/index.html', {'titulo': 'Bookflix-Librería Online'})
    
def donde_estamos(request):
    return render(request, 'books/donde_estamos.html', {'titulo': 'Bookflix-Dónde estamos'})

def catalogo(request):
    return render(request, 'books/catalogo.html', {'titulo': 'Bookflix-Catálogo'})

def crear(request):
    formulario = LibroForms(request.POST or None)
    return render(request, 'books/crear.html', {'titulo': 'Bookflix-Cargar Libro', 'formulario': formulario})

def editar(request):
    return render(request, 'books/editar.html', {'titulo': 'Bookflix-Editar Libro'})

def eliminar(request):
    pass