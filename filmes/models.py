from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
       return self.nome
    
class Filme(models.Model):
    titulo = models.CharField(max_length=150)
    ano = models.IntegerField()
    diretor = models.CharField(max_length=100, default="Desconhecido")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo