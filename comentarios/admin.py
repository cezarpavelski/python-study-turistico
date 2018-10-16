from django.contrib import admin

from comentarios.actions import reprovar_comentarios, aprovar_comentarios
from .models import Comentario


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'data', 'aprovado')
    actions = (reprovar_comentarios, aprovar_comentarios)

admin.site.register(Comentario, ComentarioAdmin)
