from rest_framework.viewsets import ModelViewSet
from evento.api.serializers import EventosSerializer
from evento.models import Evento


class EventoViewSet(ModelViewSet):

    queryset = Evento.objects.all()
    serializer_class = EventosSerializer