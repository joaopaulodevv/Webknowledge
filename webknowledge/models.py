from django.db import models
from django.contrib.auth.models import User


class Usuariosite(models.Model):
    idusuario =  models.IntegerField()
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    datadenascimento = models.DateField()
    nota = models.FloatField()
    nome = models.CharField(max_length=100)

    def avaliarusuario(self, idusuario):
      
        pass




class Aluno(models.Model):
    usuario = models.OneToOneField(
        Usuariosite,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    qtdaulasassistidas = models.IntegerField()

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

    qtdaulasfeitas = models.IntegerField()
    disciplina = models.CharField(max_length=40)
    especialidade = models.CharField(max_length=200)

    def criarPerfil(self):
        
        pass

    def darAula(self):
        
        pass

    def __str__(self):
        return f'Professor {self.usuario.nome} - Especialidade: {self.especialidade}'


class Aula(models.Model):
    dataAula = models.DateField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Aula {self.professor} - {self.dataAula}'


class Avaliacao(models.Model):  
   
    avaliada =  models.ForeignKey(Usuariosite, on_delete=models.CASCADE) 
    nota = models.FloatField()  
    comentario = models.CharField(max_length=200)

    def enviar(self):
        
        pass

    def __str__(self):
        return f'Avaliacao {self.id} - Nota: {self.nota}'
