from rest_framework.viewsets import ModelViewSet

from agendamento.models import Agendamento
from agendamento.api.serializers import AgendamentoSerializer


class AgendamentoViewSet(ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
