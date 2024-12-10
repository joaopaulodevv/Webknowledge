from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import EditarPerfilForm, NovoUsuarioForm, UsuariositeForm,ProfessorsiteForm,MensagemForm
from .models import Usuariosite , Professor, Aluno, Conversa, Mensagem
from django.contrib.auth.models import User
from django.db.models import Q


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
        primeirologin(request)

        return redirect('/minhaconta/')  

    return render(request, 'cadastro.html', {
        'form': user_form,
        'form2': usuariosite_form,
    })




def sobrenos(request):
    return render(request,"sobre_nos2.0.html")

@login_required
def homealuno(request):
    busca = request.GET.get('busca', '')
    usuarios = Usuariosite.objects.filter(tipo_conta="professor")
    if busca:
        usuarios = usuarios.filter(
            Q(nome__icontains=busca) |  
            Q(professor__disciplina__icontains=busca) |  
            Q(professor__especialidade__icontains=busca) 
        )

    context = {
        'meuuser': request.user.usuariosite,
        'usuarios': usuarios,
        'busca': busca, 
    }
    return render(request, 'homealuno.html', context)

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
    usuario = request.user.usuariosite  
    user = Usuariosite.objects.get(id=iduser)
    return render(request,"professores.html",{"prof":user,"id":iduser,"usuario":usuario })


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

def lista_conversas(request):
    if request.user.is_authenticated:
        usuario = request.user.usuariosite
        
        if hasattr(usuario, 'aluno'): 
            conversas = Conversa.objects.filter(aluno=usuario.aluno).select_related('professor__usuario')
        elif hasattr(usuario, 'professor'): 
            conversas = Conversa.objects.filter(professor=usuario.professor).select_related('aluno__usuario')
        else:
            return redirect('/')
        
        return render(request, 'listaconversas.html', {'conversas': conversas, 'usuario': usuario})
    
    return redirect('/')



@login_required
def nova_conversa(request, professor_id):
    professor = get_object_or_404(Professor, usuario_id=professor_id)  # Corrigido aqui
    aluno = request.user.usuariosite.aluno  

    conversa, created = Conversa.objects.get_or_create(aluno=aluno, professor=professor)

 
    return redirect('detalhe_conversa', conversa_id=conversa.id)

@login_required
def detalhe_conversa(request, conversa_id):
    conversa = get_object_or_404(Conversa, id=conversa_id)
    usuariosite = request.user.usuariosite

    if hasattr(usuariosite, 'aluno'):  
        outro_participante = conversa.professor.usuario
    elif hasattr(usuariosite, 'professor'):  
        outro_participante = conversa.aluno.usuario
    else:
        outro_participante = None

    if request.method == "POST":
        form = MensagemForm(request.POST)
        if form.is_valid():
            mensagem = form.save(commit=False)
            mensagem.conversa = conversa
            mensagem.remetente = usuariosite
            mensagem.save()
            return redirect('detalhe_conversa', conversa_id=conversa.id)
    else:
        form = MensagemForm()

    mensagens = Mensagem.objects.filter(conversa=conversa)

    return render(request, 'detalhe_conversa.html', {
        'conversa': conversa,
        'mensagens': mensagens,
        'form': form,
        'outro_participante': outro_participante,  # Enviar o outro participante
    })
