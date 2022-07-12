from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'books/index.html', {'titulo': 'Bookflix-Librería Online'})
    
def donde_estamos(request):
    return render(request, 'books/donde_estamos.html', {'titulo': 'Bookflix-Dónde estamos'})

def catalogo(request):
    return render(request, 'books/catalogo.html', {'titulo': 'Bookflix-Catálogo'})

def crear(request):
    return render(request, 'books/crear.html', {'titulo': 'Bookflix-Cargar Libro'})

def editar(request):
    return render(request, 'books/editar.html', {'titulo': 'Bookflix-Editar Libro'})

def eliminar(request):
    pass