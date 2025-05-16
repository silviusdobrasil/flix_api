from django.contrib import admin
from .models import Avaliacoes

@admin.register(Avaliacoes)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id','nota')
    search_fields  = ('id', 'nota')       
    