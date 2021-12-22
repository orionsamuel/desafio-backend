from django.db import models

# Create your models here.
class Alunos(models.Model):
    pasta = models.IntegerField()
    ano = models.IntegerField()
    nome = models.CharField(max_length=150)
    filiacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome