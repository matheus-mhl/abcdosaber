from django.urls import path
from . import views

app_name = 'instrutores'

urlpatterns = [
    path('lista/', views.listar, name = 'listar'),
    
    

]