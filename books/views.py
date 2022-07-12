from django.shortcuts import redirect, render
from django.http import HttpResponse
from books.models import Libro

from books.forms import LibroForms


# Create your views here.
def index(request):
    return render(request, 'books/index.html', {'titulo': 'Bookflix-Librería Online'})
    
def donde_estamos(request):
    return render(request, 'books/donde_estamos.html', {'titulo': 'Bookflix-Dónde estamos'})

def catalogo(request):
    libros = Libro.objects.all()
    return render(request, 'books/catalogo.html', {'titulo': 'Bookflix-Catálogo', 'libros': libros})

def gestion(request):
    libros = Libro.objects.all()
    return render(request, 'books/gestion_catalogo.html', {'titulo': 'Bookflix-Catálogo', 'libros': libros})

def crear(request):
    formulario = LibroForms(request.POST or None, request.FILES or None) #que tome datos y archivos del formulario
    if formulario.is_valid():
        formulario.save()
        return redirect('gestion_catalogo')
    return render(request, 'books/crear.html', {'titulo': 'Bookflix-Cargar Libro', 'formulario': formulario})

def editar(request):
    return render(request, 'books/editar.html', {'titulo': 'Bookflix-Editar Libro'})

def eliminar(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    libro.delete()
    return redirect('gestion_catalogo')