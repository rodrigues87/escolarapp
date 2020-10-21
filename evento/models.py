from django.db import models


# Create your models here.

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
