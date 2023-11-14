from ast import If
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from usuarios.forms import CadastroForms, LoginForms
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def login(request):
  form = LoginForms()
  if request.method == 'POST':
    form = LoginForms(request.POST)
    if form.is_valid():
      nome = form['nome_login'].value()
      senha = form['senha'].value()
    
    usuario = auth.authenticate(
      request,
      username = nome,
      password = senha,
    )
    if usuario is not None:
      auth.login(request, usuario)
      return redirect('home')
    else:
      return redirect('login')

  return render(request, "usuarios/login.html",{"form":form})

def cadastro(request):
  form = CadastroForms()

  if request.method == 'POST':
    form = CadastroForms(request.POST)
    if form.is_valid():
      if form['senha_1'].value() != form['senha_2'].value():
        return redirect('cadastro')
      nome=form['nome_cadastro'].value()
      email=form['email'].value()
      senha_1=form['senha_1'].value()

      if User.objects.filter(username=nome).exists():
        return redirect('cadastro')
      
      usuario = User.objects.create_user(
        username=nome,
        email=email,
        password=senha_1
      )
      usuario.save()
      return redirect('login')

  return render(request, "usuarios/cadastro.html",{"form":form})
  