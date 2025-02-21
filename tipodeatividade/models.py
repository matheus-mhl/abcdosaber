from django.db import models
from django.urls import reverse

# Create your models here.
class TipoDeAtividade(models.Model):
    """Modeli representando um Tipo de Atividade"""
    codigo = models.IntegerField(primary_key=True,
                                 help_text='Código do Tipo de atividade')
    descricao = models.CharField(max_length=100, null=False,
                                 help_text='Informe a descrição do Tipo de Atividade')
    
    def __str__(self):
        return f'{self.codigo} {self.descricao}'
