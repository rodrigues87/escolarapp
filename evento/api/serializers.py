from rest_framework.serializers import ModelSerializer
from evento.models import Evento, Favorito


class EventosSerializer(ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'


class FavoritosSerializer(ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'
