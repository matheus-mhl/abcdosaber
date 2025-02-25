from django.shortcuts import render
from django.http import HttpResponse
from titulos.models import Titulos
from titulos.forms import TitulosForm


# Create your views here.
def listar(request):
    return render (request, 'titulos/listar_titulos.html')

def carregar_cadastro(request):
    return render (request, 'titulos/cadastrar_titulos.html')

def cadastrar(request):
    form = TitulosForm(request.POST)
    if form.is_valid():
        dados_titulos = form.cleaned_data
        titulos = Titulos(
            descricao = dados_titulos['descricao']
        )
        titulos.save()
        
    return render(request, 'titulos/cadastrar_titulos.html')