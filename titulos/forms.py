from django import forms

class TitulosForm(forms.Form):
    codigo = forms.IntegerField(required=True,
                                 help_text='Código do Titulos')
    descriçao = forms.CharField(max_length=100, required=True,
                                 help_text='Informe a descrição de Titulos')