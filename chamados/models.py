from django.db import models

from usuarios.models import User


class Impressora(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ("F", "FUNCIONANDO"),
        ("D", "DEFEITO"),
        ("R", "REPARO")
    )
    status_impressora = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __int__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Impressoras"


class Chamado(models.Model):
    titulo = models.CharField(max_length=40)
    descricao = models.CharField(max_length=250)
    impressora = models.ForeignKey(Impressora, on_delete=models.CASCADE)
    dataAbertura = models.DateField(auto_now_add=True, blank=True)
    horarioAbertura = models.TimeField(auto_now_add=True, blank=True)

    def __int__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Chamados"
