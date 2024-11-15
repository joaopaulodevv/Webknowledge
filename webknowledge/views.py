from django.shortcuts import render, redirect
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


def index(request):
  formulario = AuthenticationForm()
  if request.method == 'POST' and request.POST:
    formulario = AuthenticationForm(request, request.POST)
    if formulario.is_valid(): 
      usuario = formulario.get_user()
      login(request, usuario)
      return redirect('homealuno/')
  return render(request, 'index.html', {'formulario': formulario})







def cadastro(request):
    return render(request,"cadastro.html")


def sobrenos(request):
    return render(request,"sobrenos.html")

@login_required
def homealuno(request):
    return render(request,"homealuno.html")


@login_required
def logout_usuario(request):
    logout(request)
    request.session.flush()  # Limpa completamente a sessão
    return redirect('/')