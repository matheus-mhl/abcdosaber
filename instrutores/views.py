from django.shortcuts import render
from django.http import HttpResponse

from instrutores.models import Instrutores
from titulos.models import Titulos
from instrutores.forms import InstrutoresForm

# Create your views here.
def listar(request):
    lista_instrutores = Instrutores.objects.all()
    contexto = {
        'instrutores' : lista_instrutores
    }
    
    return render (request, 'instrutores/listar_instrutores.html', context = contexto)

def carregar_cadastro(request):
    lista_titulos = Titulos.objects.all()
    contexto = {
        'titulos': lista_titulos
    }
    return render (request, 'instrutores/cadastrar_instrutores.html', context=contexto)

def cadastrar(request):
    form = InstrutoresForm(request.POST)
    if form.is_valid():
        dados_instrutores = form.cleaned_data
        titulos = Titulos.objects.get(pk=dados_instrutores["codigo_titulos"])
        
        instrutores = Instrutores(
            rg = dados_instrutores["rg"],
            nome = dados_instrutores["nome"],
            data_Nascimento = dados_instrutores["data_Nascimento"],
            telefone = dados_instrutores["telefone"],
            ddd = dados_instrutores [ "ddd"],
            codigo_titulo = titulos,
        )
        instrutores.save()
    
    return render(request, 'instrutores/cadastrar_instrutores.html')

