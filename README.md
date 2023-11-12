# Projeto de curso DJANGO
Trata-se de um projeto django com duas páginas html exibindo imagens staticas.

Para este projeto funcioanr é necessário:
- Clonar projeto do github
- Abrir o projeto no vscode
- Criar e ativar ambiente virtual
- Instalar dependendias com freeze `pip install -r requirements.txt`
- Execultar `python manage.py runserver`

## Orientações diversas
- Instalação e ativação do pacote gerenciador do ambiente virtual
```
pip install virtualenv
virtualenv venv
venv/Scripts/activate
```
- Instação do django
```
pip install django
```
- Verificando dependencias necessarias para o projeto
```
pip freeze
```
- Arquivo de requerimentos para o projeto (instalação automatica de pacotes)
  - Criar arquivo
  ```
  pip freeze > requirements.txt
  ```
  - Instala os pacotes com base no arquivo criado
  ```
  pip install -r requirements.txt
  ```
- Verificando comandos do Django
```
django-admin help
```
- Iniciando projeto
```
django-admin startproject setup .
```
- Start projeto
```
python manage.py runserver
```
- Alterar as configuraçãoes do projeto no arquivo settings dentro da pasta setup
  - Idioma - LANGUAGE_CODE
  - Zona (horario) - TIME_ZONE
  - Secret-Key
    - Usar variaveis de ambiente para modo dev, a key nao deve ser enviada para o git em produção
    - `pip install python-dotenv`
    - Criar arquivo .env e armazerar a key dentro dele
    - No arquivo settings apos o import do Path, fazer o import os
    - `import os`
    - Fazer o import do dotenv
    - `from dotenv import load_dotenv`
    - Chamar o load dentro do arquivo settings
    - `load_dotenv()`
    - Importar a key que esta no arquivo .env na SECRET_KEY
    - `str(os.getenv('SECRET_KEY'))`
    - Incluir apps adicionados na lista INSTALLED_APPS
- Criar novo app dentro do projeto
```
python manage.py startapp galeria
```
- Na pasta do app criado há um arquivo view.py, ele é responsavel pela exibição do conteudo do projeto/app
- Para definir as rotas, deve ser configurado o arquivo url.py dentro da pasta setup
  - Para isto, não esquecer de importar o arquivo que contem o conteudo a ser exibido, arquivo view.py dentro da pasta de app criada
  - Porem é uma boa pratica criar um arquivo urls.py dentro de cada app, assim rodas relecionadas a este app ficam encapsuladas em um só lugar, deixando limpo de codigo extra o arquivo urls.py que esta dentro de setup
  - No arquivo urls.py da pasta setup, incluir na importação do path o include e na lista de rotas incluir o caminho para o arquivo urls.py do app
    - ```path('', include('galeria.urls'))```
- Em TEMPLATES, no arquivo settings dentro de setup é usado o "DIRS" que contem uma lista.
  -  Nesta lista é feito um join para configurar a pasta de templetes do app, para isso usamos novamente a biblioteca os ja importada anteriomente ```os.path.join(BASE_DIR, "templates")```
     -  BASE_DIR é o diretorio principal (root do projeto)
  -  Para importação de estilos e pastas com imagens por exemplo, usamos a variavel STATIC_URL dentro de settings na pasta setup
     -  Logo abaixo da variavel indicada criar uma nova qque ira contem uma lista seu nome sera STATICFILES_DIRS.
     -  Dentro da pasta setup criar uma pasta de nome static
     -  Passar o caminho da pasta criada usando a biblioteca os `os.path.join(BASE_DIR, 'setup/static')`
     -  Criar nova variavel no arquivo settings seu nome sera STATIC_ROOT, passar caminho para esta variavel `os.path.join(BASE_DIR, 'static')`
     -  Inserir as pastas de assets e style dentro da pasta static criada na pasta setup
     -  Inserir comando para django setar as configurações de estilo ```python manage.py collectstatic```
     -  No top do arquivo html inserit linha de codigo que faz carregamento das confdigurações ```{% load static %}```
     -  Configurar a tag com caminho da pasta no arquivo html
        -  Exemplo no head do html configuração para aceitar os styles : `<link rel="stylesheet" href="{% static 'styles/style.css' %}">`
        -  Exemplo para exibição das imagens: `<a href="#"><img src="{% static '/assets/ícones/1x/Home - ativo.png' %}"> Home</a>`