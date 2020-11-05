from django.db import models

from usuarios.models import User


class Agendamento(models.Model):
    nome_agendamento = models.CharField(max_length=40)
    data = models.DateField()
    horainicio = models.TimeField()
    horafinal = models.TimeField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.nome_agendamento

    class Meta:
        verbose_name_plural = "Agendamentos"
