from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia


def index(request):
  fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

  return render(request, "galeria/index.html", {"cards": fotografias})


def imagem(request, foto_id):
    # fotografias = Fotografia.objects.all()
    # print(fotografias)
    # foto = fotografias.filter(id=foto_id).first()
    # print(foto)
    foto = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, "galeria/imagem.html", {"foto":foto})

def buscar(request):
  fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
  if "buscar" in request.GET:
     nome_buscado = request.GET['buscar']
     if nome_buscado:
        fotografias = fotografias.filter(nome__icontains=nome_buscado)
  return render(request, 'galeria/buscar.html', {"cards": fotografias})


