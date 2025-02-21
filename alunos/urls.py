from django.urls import path
from . import views

app_name = 'alunos'

urlpatterns = [
    path('listar', views.listar, name = 'listar'),
    
    

]