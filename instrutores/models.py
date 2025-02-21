from django.db import models
from titulos.models import Titulos

class Instrutores(models.Model):
    id = models.BigAutoField(primary_key=True)
    rg = models.CharField(max_length=20)
    nome = models.CharField(max_length=100, null=True, blank=True)
    data_nascimento = models.DateField(null=True)
    telefone = models.CharField(max_length=15)
    ddd = models.CharField(max_length=3, null=True, blank=True)
    codigo_titulos = models.ForeignKey(Titulos, 
                                       on_delete=models.SET_NULL,
                                       null = True, 
                                       blank=True,
                                       )
   

    def __str__(self):
        return f"{self.nome} - {self.rg}"


