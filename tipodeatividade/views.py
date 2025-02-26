from django.shortcuts import render
from django.http import HttpResponse
from tipodeatividade.models import TipoDeAtividade

app_name  = 'tipodeatividade'

# Create your views here.
def listar(request):
    lista_tipodeatividade = TipoDeAtividade.objects.all()
    context = {
        'tipodeatividade' : lista_tipodeatividade,
    }
    
    return render(request, 'tipodeatividade/listar_tipodeatividade.html', context)

# chamada para carregar a pagina de cadastro no navegador
def carregar_cadastro(request):
    return render (request, 'tipodeatividade/cadastrar_tipodeatividade.html')


