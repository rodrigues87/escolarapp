from django.db import models


class Tarefa(models.Model):
    realizada = models.BooleanField(default=False)
    descricao = models.CharField(max_length=40)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Tarefas"
