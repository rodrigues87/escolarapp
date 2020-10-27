from rest_framework.serializers import ModelSerializer
from tarefas.models import Tarefa


class TarefasSerializer(ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'
