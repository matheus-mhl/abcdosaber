from django.shortcuts import render
from django.http import HttpResponse

from instrutores.models import Instrutores

# Create your views here.
def listar(request):
    lista_instrutores = Instrutores.object.all()
    return HttpResponse(lista_instrutores)
