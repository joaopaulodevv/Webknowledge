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
    descricao = models.TextField(null=True, blank=True, max_length=900)
    def criarPerfil(self):
        pass

    def darAula(self):
        pass

    def __str__(self):
        return f'Professor {self.usuario.nome} - Especialidade: {self.especialidade}'


class Conversa(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="conversas_aluno")
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="conversas_professor")
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversa entre {self.aluno.username} e {self.professor.username} - {self.criada_em}"
    

class Mensagem(models.Model):
    conversa = models.ForeignKey(Conversa, on_delete=models.CASCADE, related_name="mensagens")
    remetente = models.ForeignKey(Usuariosite, on_delete=models.CASCADE)
    texto = models.TextField()
    enviada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.remetente.username} em {self.enviada_em}"