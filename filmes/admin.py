from django.contrib import admin
from .models import Filmes

@admin.register(Filmes)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'genero', 'data_lancamento', 'resumo')
  
    search_fields = ('titulo',)
    list_filter = ('titulo', 'genero', 'data_lancamento')
    ordering = ('titulo', 'data_lancamento')
    list_per_page = 10