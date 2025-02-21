from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Olá, Matheus!!")

def listar(request):
    return HttpResponse("Lista de Tipos de Aividade")

def show_mensagem(request):
    x = 'M'
    nome = x + "atheus, tudo certo?"
    return HttpResponse(f"Bom dia!{nome}")

# Nova função para exibir uma lista de atividades
def listar_atividades(request):
    atividades = [
        "Correr",
        "Nadar",
        "Estudar",
        "Ler",
        "Jogar futebol",
    ]
    
    # Criando a resposta para exibir a lista de atividades
    resposta = "<h1>Lista de Atividades</h1>"
    resposta += "<ul>"
    for atividade in atividades:
        resposta += f"<li>{atividade}</li>"
    resposta += "</ul>"
    
    return HttpResponse(resposta)