from django.db import models


class Remedio(models.Model):
    nome = models.CharField(max_length=40)
    mg = models.DecimalField(max_digits=4, decimal_places=2)
    qnt_comprimidos = models.IntegerField()
    intervalo = models.CharField(max_length=40)
    horario_inicial = models.CharField(max_length=40)
    horario_de_tomar = models.CharField(max_length=40)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Remedios"
