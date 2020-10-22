from rest_framework.viewsets import ModelViewSet
from evento.api.serializers import EventosSerializer, FavoritosSerializer
from evento.models import Evento, Favorito


class EventoViewSet(ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventosSerializer


class FavoritoViewSet(ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritosSerializer
