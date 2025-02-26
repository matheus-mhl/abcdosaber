from django.shortcuts import render
from django.http import HttpResponse
from titulos.models import Titulos
from titulos.forms import TitulosForm


# Create your views here.
def listar(request):
    lista_titulos = Titulos.objects.all()
    context = {
        'titulos': lista_titulos,
    }
    return render (request, 'titulos/listar_titulos.html', context)

# chamada para carregar a pagina de cadastro no navegador
def carregar_cadastro(request):
    return render (request, 'titulos/cadastrar_titulos.html')

# chamada para processar os dados do formulario
# devolve a pagina de cadastro para novo cadastramento
def cadastrar(request):
    form = TitulosForm(request.POST)
    if form.is_valid():
        dados_titulos = form.cleaned_data
        titulos = Titulos(
            descricao = dados_titulos['descricao']
        )
        titulos.save()
    
    return render(request, 'titulos/cadastrar_titulos.html')
        
    