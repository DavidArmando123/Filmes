from django.db import models

# Create your models here.

class categorias (models.TextChoices):
    ROMANCE = 'romance','romance'
    COMEDIA = 'comedia', 'comedia'
    TERROR = 'terror', 'terror'
    DRAMA = 'drama', 'drama'
    AVENTURA = 'aventura', 'aventura'

class filmes (models.Model):
    titulo = models.CharField(max_length=100)
    ano_de_lancamento = models.IntegerField()
    descricao = models.TextField()
    categoria = models.CharField(max_length=20, choices=categorias.choices)



