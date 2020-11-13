from django.db import models

# Create your models here.
from usuarios.models import User


class Evento(models.Model):
    data = models.DateField()
    horario = models.TimeField()
    local = models.CharField(max_length=40)
    preco = models.DecimalField(max_digits=4, decimal_places=2)
    nomeEvento = models.CharField(max_length=40)

    def __str__(self):
        return self.nomeEvento

    class Meta:
        verbose_name_plural = "Eventos"


class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.email

    class Meta:
        verbose_name_plural = "Favoritos"
