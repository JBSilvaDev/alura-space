from ast import If
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import is_valid_path
from apps.galeria.forms import FotografiaForms

from apps.galeria.models import Fotografia
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.info(request, "Usuário não logado")
        return redirect("login")
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    return render(request, "galeria/index.html", {"cards": fotografias})


def imagem(request, foto_id):
    # fotografias = Fotografia.objects.all()
    # print(fotografias)
    # foto = fotografias.filter(id=foto_id).first()
    # print(foto)
    foto = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, "galeria/imagem.html", {"foto": foto})


def buscar(request):
    if not request.user.is_authenticated:
        messages.info(request, "Usuário não logado")
        return redirect("login")
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    if "buscar" in request.GET:
        nome_buscado = request.GET["buscar"]
        if nome_buscado:
            fotografias = fotografias.filter(nome__icontains=nome_buscado)
    return render(request, "galeria/index.html", {"cards": fotografias})


def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.info(request, "Usuário não logado")
        return redirect("login")
    form = FotografiaForms
    if request.method =='POST':
        form = FotografiaForms(
            request.POST, request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova imagem cadastrada')
            return redirect('home')
    return render(request,'galeria/nova_imagem.html',{'form':form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)
    if request.method ==  'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro editado!')
            return redirect('home')
    return render(request, 'galeria/editar_imagem.html', {'form':form, 'foto_id':foto_id})
    
# def remover_imagem(request, foto_id):
#     # Remove a imagem da db
#     fotografia = Fotografia.objects.get(id=foto_id)
#   os.remove(fotografia.imagem.path)
#     fotografia.delete()
#     messages.success(request, 'Imagem removida com sucesso')
#     return redirect('home')

def remover_imagem(request, foto_id):
    # Altera a publicação de imagem no site
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.publicada = not fotografia.publicada
    fotografia.save()
    messages.success(request, 'Registro removido do site com sucesso!')
    return redirect('home')

def filtro(request, categoria):
    if not request.user.is_authenticated:
        messages.info(request, "Usuário não logado")
        return redirect("login")
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True, categoria=categoria)

    return render(request, "galeria/index.html", {"cards": fotografias})
