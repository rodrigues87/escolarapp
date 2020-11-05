from rest_framework.viewsets import ModelViewSet

from agendamento.models import Agendamento
from agendamento.api.serializers import AgendamentoSerializer


class AgendamentoViewSet(ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

    def get_queryset(self):
        return Agendamento.objects.filter(usuario__isnull=True)


class MeusAgendamentoViewSet(ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

    def get_queryset(self):
        return Agendamento.objects.filter(usuario=self.request.user)
