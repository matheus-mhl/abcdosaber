from django.db import models
from django.urls import reverse

# Create your models here.
class Titulos(models.Model):
    """Modeli representando um Titulos"""
    codigo = models.IntegerField(primary_key=True,
                                 help_text='Código do Titulos')
    descricao = models.CharField(max_length=100, null=False,
                                 help_text='Informe a descrição do Titulos')
    
    def __str__(self):
        return f'{self.codigo} {self.descricao}'
