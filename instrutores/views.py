from django.shortcuts import render
from django.http import HttpResponse

from instrutores.models import Instrutores

# Create your views here.
def listar(request):
    lista_instrutores = Instrutores.objects.all()
    contexto = {
        'instrutores' : lista_instrutores
    }
    
    return render (request, 'instrutores/listarInstrutores.html', context = contexto)
