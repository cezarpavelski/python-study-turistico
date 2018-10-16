def aprovar_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=True)


def reprovar_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=False)


reprovar_comentarios.short_description = 'Reprovar Comentarios'
aprovar_comentarios.short_description = 'Aprovar Comentarios'