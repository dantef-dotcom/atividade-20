from django.contrib import admin
from .models import Diretor, Categoria, Filme


@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ("nome", "nacionalidade")
    search_fields = ("nome",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ano_lancamento", "diretor", "categoria")
    list_filter = ("categoria", "diretor")
    search_fields = ("titulo",)