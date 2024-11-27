from django.shortcuts import render, redirect
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import EditarPerfilForm, NovoUsuarioForm, UsuariositeForm,ProfessorsiteForm
from .models import Usuariosite , Professor, Aluno

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
        user = user_form.save()  # Cria o objeto User
        usuariosite = usuariosite_form.save(commit=False)  
        usuariosite.usuario = user  
        usuariosite.nome = user.username
        usuariosite.nota = 5.0  
        usuariosite.email = user.email
        usuariosite.save()  # Salva o Usuariosite associado ao User

        # Faz o primeiro login e cria objetos associados (se necessário)
        login(request, user)
        primeirologin(request)

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
    
    
    if hasattr(usuario, 'professor'):  
        professor = usuario.professor
    else:
        professor = None  
    
    if request.method == 'POST':
  
        form = EditarPerfilForm(request.POST, request.FILES, instance=usuario)
        formprof = (
            ProfessorsiteForm(request.POST, instance=professor)
            if professor
            else None  
        )
        
        if form.is_valid():  
            form.save()
            
            if formprof and formprof.is_valid():  
                formprof.save()
            
            return redirect('/homealuno/')  
            
    else:
        
        form = EditarPerfilForm(instance=usuario)
        formprof = (
            ProfessorsiteForm(instance=professor)
            if professor
            else None
        )
    
    return render(request, 'minhacontaprofessor.html', {
        'form': form,
        'formprof': formprof,
        'usuario': usuario,
    })

@login_required
def professor(request,iduser):

    user = Usuariosite.objects.get(id=iduser)
    return render(request,"professores.html",{"prof":user})


def primeirologin(request):
    usuario = request.user.usuariosite

    
    if usuario.tipo_conta == "professor":
        professor = Professor.objects.create(
            usuario=usuario,
            qtdaulasfeitas=0,
            disciplina="Indefinido", 
            especialidade="Indefinido",  
        )
    else:
            Aluno.objects.create(

                usuario= usuario,
                qtdaulasassistidas = 0



            )
