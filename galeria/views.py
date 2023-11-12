from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia


def index(request):
  fotografias = Fotografia.objects.all()

  return render(request, "galeria/index.html", {"cards": fotografias})


def imagem(request, foto_id):
    # fotografias = Fotografia.objects.all()
    # print(fotografias)
    # foto = fotografias.filter(id=foto_id).first()
    # print(foto)
    foto = get_object_or_404(Fotografia, pk=foto_id)
    print(foto)
    return render(request, "galeria/imagem.html", {"foto":foto})


