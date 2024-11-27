from django.db import models
from django.contrib.auth.models import User


class Usuariosite(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    perfil_imagem = models.ImageField(upload_to='perfil_images/', null=True, blank=True)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    datadenascimento = models.DateField()
    nota = models.FloatField()
    nome = models.CharField(max_length=100)
    
    TIPO_CONTA = (
        ('professor', 'Professor'),
        ('aluno', 'Aluno'),
    )
    tipo_conta = models.CharField(max_length=20, choices=TIPO_CONTA, default='aluno')
    def avaliarusuario(self, idusuario):
      
        pass




class Aluno(models.Model):
    usuario = models.OneToOneField(
        Usuariosite,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    qtdaulasassistidas = models.IntegerField(null=True, blank=True)

    def agendaraula(self, professor):

        pass

    def __str__(self):
        return f'{self.usuario.nome} ({self.idaluno})'


class Professor(models.Model):
    usuario = models.OneToOneField(
        Usuariosite,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    qtdaulasfeitas = models.IntegerField(null=True, blank=True)
    disciplina = models.CharField(null=True, blank=True, max_length=40, default="Indefinido") 
    especialidade = models.CharField(null=True, blank=True, max_length=200)

    def criarPerfil(self):
        pass

    def darAula(self):
        pass

    def __str__(self):
        return f'Professor {self.usuario.nome} - Especialidade: {self.especialidade}'

