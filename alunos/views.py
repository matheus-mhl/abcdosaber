from django.shortcuts import render
from django.http import HttpResponse
from alunos.models import Alunos
from titulos.models import Titulos
from alunos.forms import AlunosForm

# Create your views here.
def listar(request):
    lista_alunos = Alunos.objects.all()
    context = {
        'alunos': lista_alunos,
    }
    return render (request, 'alunos/listar_alunos.html', context=context)

def carregar_cadastro(request):
    lista_titulos = Titulos.objects.all()
    contexto = {
        'titulos': lista_titulos
    }
    return render (request, 'Alunos/cadastrar_Alunos.html', context=contexto)

def cadastrar(request):
    form = AlunosForm(request.POST)
    if form.is_valid():
        dados_Alunos = form.cleaned_data
        titulos = Titulos.objects.get(pk=dados_Alunos["codigo_titulos"])
        
        Alunos = Alunos(
            Matricula = dados_Alunos["Matricula"],
            nome = dados_Alunos["nome"],
            data_inicial = dados_Alunos["data_inicial"],
            data_final = dados_Alunos["data_final"],
        )
        Alunos.save()
    
    return render(request, 'Alunos/cadastrar_Alunos.html')