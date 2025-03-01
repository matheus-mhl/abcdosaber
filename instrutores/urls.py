from django.urls import path
from . import views

app_name = 'instrutores'

urlpatterns = [
    path('listar/', views.listar, name = 'listar'),
    path('cadastro/', views.carregar_cadastro, name = 'cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),  # Nova URL
    
    

]