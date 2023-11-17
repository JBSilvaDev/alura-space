from django.urls import path
from apps.galeria.views import \
    index, imagem, buscar, nova_imagem, editar_imagem, remover_imagem, filtro

urlpatterns = [
    path('', index, name='home'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('nova-imagem', nova_imagem, name='nova_imagem'),
    path('editar-imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),
    path('remover-imagem/<int:foto_id>', remover_imagem, name='remover_imagem'),
    path('filtro/<str:categoria>', filtro, name='filtro'),
]