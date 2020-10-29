from django.contrib.postgres.fields import ArrayField
from django.db import models

from usuarios.models import User


class Horario(models.Model):
    horario = models.CharField(max_length=40)

    def __str__(self):
        return str(self.horario)


class Remedio(models.Model):
    nome = models.CharField(max_length=40)
    mg = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name_plural = "Remedios"


class Recomendacao(models.Model):
    remedio = models.ForeignKey(Remedio, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    qnt_comprimidos = models.IntegerField()
    intervalo = models.IntegerField()
    horario_inicial = models.TimeField()
    dose = models.IntegerField()

    def __str__(self):
        return self.remedio.nome

    class Meta:
        verbose_name_plural = "Recomendações"
