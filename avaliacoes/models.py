from django.db import models
from filmes.models import Filmes

NOTAS = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),

)

class Avaliacoes(models.Model):

    filme = models.ForeignKey(Filmes, 
                              on_delete=models.PROTECT, 
                              related_name='avaliacoes'
                              )
    nota = models.IntegerField(choices=NOTAS, blank=False, null=False)
    comentario = models.TextField(blank=True, null=True)   


    def __str__(self):
        return self.filme.titulo
