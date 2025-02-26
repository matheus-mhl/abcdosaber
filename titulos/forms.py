from django import forms

class TitulosForm(forms.Form):
    descricao = forms.CharField(max_length=100, required=True,
                                 help_text='Informe a descrição de Titulos')