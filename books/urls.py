from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('inicio/', views.index, name='inicio'),
    path('donde_estamos/', views.donde_estamos, name='donde_estamos'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('crear/', views.crear, name='crear_libro'),
    path('editar/', views.editar, name='editar_libro'),
    path('eliminar/', views.eliminar, name='eliminar_libro'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


