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
    return render(request, "galeria/buscar.html", {"cards": fotografias})


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

def editar_imagem(request):
    pass

def remover_imagem(request):
    pass