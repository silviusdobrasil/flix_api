from django.contrib import admin
from .models import Genero

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('nome',)
    ordering = ('id',)
    list_per_page = 10
