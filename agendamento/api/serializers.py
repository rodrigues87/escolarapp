from rest_framework.serializers import ModelSerializer

from agendamento.models import Agendamento


class AgendamentoSerializer(ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'
