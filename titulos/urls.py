from django.urls import path
from . import views

app_name  = 'titulos'

urlpatterns = [
    path('lista/', views.listar, name = 'listar'),
    path('cadastro/', views.carregar_cadastro, name = 'cadastro'),
    path('atividades/', views.cadastrar, name='cadastrar'),  # Nova URL
    

]