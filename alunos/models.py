from django.db import models
from django.urls import reverse

class Alunos(models.Model):
    matricula = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=70, null=True, blank=True)
    data_inicial = models.DateField(null=True)
    data_final = models.DateField(null=True)
    
   

    def __str__(self):
        return f"{self.nome} - {self.rg}"
