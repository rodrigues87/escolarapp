from rest_framework.serializers import ModelSerializer
from evento.models import Evento


class EventosSerializer(ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'
