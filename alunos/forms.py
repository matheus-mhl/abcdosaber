from django import forms

class AlunosForm(forms.Form):
    Matricula = forms.CharField(max_length=15, required=False, help_text="Informe o RG do Instrutor")
    nome = forms.CharField(max_length=70,required=False, help_text="Informe o nome do Instrutor")
    data_inicial = forms.DateField(required=True, help_text="Informe a data de nascimento do Instrutor")
    data_final = forms.CharField(max_length=9, required=False, help_text="Informe o telefone do Instrutor")
    