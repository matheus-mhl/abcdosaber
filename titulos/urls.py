from django.urls import path
from . import views

app_name  = 'titulos'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('lista/', views.listar, name = 'listar'),
    path('bomdia/', views.show_mensagem, name = 'bomdia'),
    path('atividades/', views.listar_atividades, name='listar_atividades'),  # Nova URL
    

]