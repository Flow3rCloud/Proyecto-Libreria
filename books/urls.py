from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('inicio/', views.index, name='inicio'),
    path('donde_estamos/', views.donde_estamos, name='donde_estamos'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('crear/', views.crear, name='crear'),
    path('editar/', views.editar, name='editar'),
    path('eliminar/', views.eliminar, name='eliminar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


