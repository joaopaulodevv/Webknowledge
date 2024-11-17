from django import forms
from .models import Professor, Aluno, Usuariosite
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EditarPerfilForm(forms.ModelForm):
           
    class Meta():
        model = Usuariosite
        fields = ['nome', 'email', 'cpf', 'datadenascimento',"nome",
    "tipo_conta"]

class NovoUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    nome = forms.CharField(max_length=150)
    class Meta:
        model = User
        fields = ['username',"nome", 'email','password1', 'password2']