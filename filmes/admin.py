from django.contrib import admin
from .models import Categoria, Filme

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
   list_display = ('id', 'nome')
   search_fields = ('nome',)

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
   list_display = ('id', 'titulo', 'ano', 'categoria')
   search_fields = ('titulo',)
   list_filter = ('categoria',)