from rest_framework.viewsets import ModelViewSet
from tarefas.api.serializers import TarefasSerializer
from tarefas.models import Tarefa


class TarefeViewSet(ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefasSerializer
