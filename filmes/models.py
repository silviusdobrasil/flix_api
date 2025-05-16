from django.db import models
from atores.models import Atores
from genero.models import Genero

class Filmes(models.Model):
    titulo = models.CharField(max_length=500)
    genero = models.ForeignKey(Genero, 
                               on_delete=models.PROTECT,
                               related_name='filmes',
                               )
    data_lancamento = models.DateField(null=True, blank=True)
    atores = models.ManyToManyField(Atores,
                               related_name='atores',
                               blank=True,
                               null=True,
                               )
    resumo = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.titulo