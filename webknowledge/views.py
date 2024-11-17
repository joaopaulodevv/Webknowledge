from django.shortcuts import render, redirect
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import EditarPerfilForm, NovoUsuarioForm
from .models import Usuariosite

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
    formulario = NovoUsuarioForm()
    if request.method == 'POST' and request.POST:
        formulario = NovoUsuarioForm(request.POST)
        if formulario.is_valid():
            novo_usuario = formulario.save(commit=False)
            novo_usuario.email = formulario.cleaned_data['email']
            novo_usuario.nome = formulario.cleaned_data["nome"]
            novo_usuario.save()
            return redirect('/login')
    return render(
request, 'cadastro.html',
{'formulario': formulario}
)




    return render(request,"cadastro.html")


def sobrenos(request):
    return render(request,"sobrenos.html")

@login_required
def homealuno(request):
    return render(request,"homealuno.html")


@login_required
def logout_usuario(request):
    logout(request)
    request.session.flush()
    return redirect('/')


@login_required
def editar_perfil_prof(request):
    usuario = request.user.usuariosite
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            
            return redirect('/homealuno/')  
    else:
        form = EditarPerfilForm(instance=usuario)
    
    return render(request, 'minhacontaprofessor.html', {'form': form})