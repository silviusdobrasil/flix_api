from django.db import models

NACIONALIDADE_CHOICES = (
    (1, 'Brasil'),
    (2, 'Estados Unidos'),
    
)


class Atores(models.Model):
    nome = models.CharField(max_length=200)
    aniversario = models.DateField(null=True, blank=True)
    nacionalidade = models.IntegerField(
        choices=NACIONALIDADE_CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.nome
