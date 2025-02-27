from django.shortcuts import render
from django.http import HttpResponse
from tipodeatividade.models import TipoDeAtividade
from tipodeatividade.forms import TipoDeAtividadeForm

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

# chamada para processar os dados do formulario
# devolve a pagina de cadastro para novo cadastramento
def cadastrar(request):
    form = TipoDeAtividadeForm(request.POST)
    if form.is_valid():
        dados_tipodeatividade = form.cleaned_data
        tipodeatividade = TipoDeAtividade(
            descricao = dados_tipodeatividade['descricao']
        )
        tipodeatividade.save()
    
    return render(request, 'tipodeatividade/cadastrar_tipodeatividade.html')


