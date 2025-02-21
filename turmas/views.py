from django.shortcuts import render
from django.http import HttpResponse

from turmas.models import Turmas

# Create your views here.

def listar(request):
    lista_turmas = Turmas.objects.all()
    return HttpResponse(lista_turmas)