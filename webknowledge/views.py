from django.shortcuts import render, redirect
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import EditarPerfilForm, NovoUsuarioForm, UsuariositeForm
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
    user_form = NovoUsuarioForm(request.POST)
    usuariosite_form = UsuariositeForm(request.POST)
    
    if user_form.is_valid() and usuariosite_form.is_valid():
        user = user_form.save()  
        usuariosite = usuariosite_form.save(commit=False)  
        usuariosite.usuario = user  
        usuariosite.nome = user.username
        usuariosite.nota = 5.0  
        usuariosite.email = user.email
        usuariosite.save()  

        login(request, user)  
        return redirect('/minhaconta/')  

    return render(request, 'cadastro.html', {
        'form': user_form,
        'form2': usuariosite_form,
    })



def sobrenos(request):
    return render(request,"sobrenos.html")

@login_required
def homealuno(request):

    usuarios  = Usuariosite.objects.filter(tipo_conta="professor")
    meuusuario = request.user.usuariosite
   

    return render(request,"homealuno.html",{"usuarios": usuarios, "meuuser":meuusuario})


@login_required
def logout_usuario(request):
    logout(request)
    request.session.flush()
    return redirect('/')


@login_required
def editar_perfil_prof(request):
    usuario = request.user.usuariosite
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            
            return redirect('/homealuno/')  
    else:
        form = EditarPerfilForm(instance=usuario)
    
    return render(request, 'minhacontaprofessor.html', {'form': form})


def professor(request):
    return render(request,"professores.html")