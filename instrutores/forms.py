from django import forms

class InstrutoresForm(forms.Form):
    rg = forms.CharField(max_length=15, required=False, help_text="Informe o RG do Instrutor")
    nome = forms.CharField(max_length=70,required=False, help_text="Informe o nome do Instrutor")
    dataNascimento = forms.DateField(required=True, help_text="Informe a data de nascimento do Instrutor")
    telefone = forms.CharField(max_length=9, required=False, help_text="Informe o telefone do Instrutor")
    ddd = forms.CharField(max_length=3, required=False, help_text="Informe o DDD do telefone do Instrutor")
    codigo_titulo = forms.IntegerField(required=True, help_text="informe o título do Instrutor")