from django.contrib import admin
from .models import Familias

@admin.register(Familias)
class FamiliasAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'slug', 'rua', 'cidade', 'renda', 'comentario', 'criado_em', 'atualizado_em']
    list_filter = ['criado_em']
    list_editable = ['nome','slug','rua', 'cidade', 'renda', 'comentario']
    prepopulated_fields = {'slug': ('nome',)}