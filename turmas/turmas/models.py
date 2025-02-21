from django.db import models
from titulos.models import Titulos

class Turmas(models.Model):
    numero = models.BigAutoField(primary_key=True)
    horarioAula = models.TimeField(max_length=70, null=True, blank=True)
    duraçaoAula = models.DurationField(null=True)
    data_inicial = models.DateField(null=True)
    dataFinal = models.DateField (null=True)
    
    def __str__(self):
        return f"{self.nome} - {self.rg}"

