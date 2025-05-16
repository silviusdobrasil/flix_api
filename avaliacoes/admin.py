from django.contrib import admin
from .models import Avalicoes

@admin.register(Avalicoes)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id','nota')
    search_fields  = ('id', 'nota')       
    