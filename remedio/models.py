from datetime import timedelta

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
    intervalo = models.IntegerField()
    dias = models.IntegerField()
    ultima_hora_que_tomou = models.DateTimeField(null=True, blank=True)
    quantidade_total_comprimidos = models.IntegerField(null=True, blank=True)
    quantidade_tomada_comprimidos = models.IntegerField(default=0)
    quantidade_restante = models.IntegerField(null=True, blank=True)
    proximo_horario = models.DateTimeField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.remedio.nome

    def save(self, *args, **kwargs):
        self.quantidade_total_comprimidos = (24/self.intervalo) * self.dias
        self.proximo_horario = self.ultima_hora_que_tomou + timedelta(hours=self.intervalo)
        try:
            recomendacao = Recomendacao.objects.get(id=self.id)
            if recomendacao.ultima_hora_que_tomou != self.ultima_hora_que_tomou:
                self.quantidade_tomada_comprimidos = self.quantidade_tomada_comprimidos + 1
                self.quantidade_restante = self.quantidade_total_comprimidos - self.quantidade_tomada_comprimidos
                if self.quantidade_restante <= 0:
                    self.delete()
                    return
        except Recomendacao.DoesNotExist:
            listing = None

        super(Recomendacao, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Recomendações"
