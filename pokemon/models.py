from django.db import models


class Tipo(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Tipos"


class Pokemon(models.Model):
    nome_pokemon = models.CharField(max_length=40)
    idade = models.IntegerField()
    tamanho = models.IntegerField()
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.nome_pokemon

    class Meta:
        verbose_name_plural = "Pokemons"
