from django.contrib import admin
from .models import Usuariosite


class UsuariositeAdmin(admin.ModelAdmin):
    list_display = ("usuario",
    "email",
    "cpf",
    "datadenascimento" ,
    "nota" ,
    "nome",
    "tipo_conta" )


admin.site.register(Usuariosite, UsuariositeAdmin)


