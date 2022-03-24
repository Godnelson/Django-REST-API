from tkinter import CASCADE
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Filmes(models.Model):
    name = models.CharField(max_length=255)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Assinatura(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.DecimalField(decimal_places=2,max_digits=5, default=0)
    def __str__(self):
        return self.nome

class Usuarios(models.Model):
    nome = models.CharField(max_length=255)
    assinatura_fk = models.ForeignKey(Assinatura, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Favoritos(models.Model):
    filme_id = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    idUser = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    def __str__(self):
        return '{},{}'.format(self.idUser,self.filme_id)

