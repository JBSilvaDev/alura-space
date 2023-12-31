from django.shortcuts import redirect, render


from apps.usuarios.forms import CadastroForms, LoginForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# Create your views here.
def login(request):
    form = LoginForms()
    if request.method == "POST":
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha"].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha,
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"Bem vindo {nome}!")
            return redirect("home")
        else:
            messages.error(request, "Usuário ou senha inválidos")
            return redirect("login")

    return render(request, "usuarios/login.html", {"form": form})


def cadastro(request):
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)
        if form.is_valid():
            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha_1 = form["senha_1"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, f"Usuário {nome} não está disponível!")
                return redirect("cadastro")

            usuario = User.objects.create_user(
                username=nome, email=email, password=senha_1
            )
            usuario.save()
            messages.success(request, f"Cadastro realizado com sucesso ➡️ {nome}!")
            return redirect("login")

    return render(request, "usuarios/cadastro.html", {"form": form})


def logout(request):
    if not request.user.is_authenticated:
        messages.info(request, "Usuário não logado, desnecessário fazer logout")
        return redirect("login")
    auth.logout(request)
    messages.info(request, "Você saiu...")
    return redirect("login")
