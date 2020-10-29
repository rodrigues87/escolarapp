from rest_framework.viewsets import ModelViewSet

from remedio.api.serializers import RemedioSerializer, RecomendacaoSerializer
from remedio.models import Remedio, Recomendacao


class RemedioViewSet(ModelViewSet):
    queryset = Remedio.objects.all()
    serializer_class = RemedioSerializer


class RecomendacaoViewSet(ModelViewSet):
    queryset = Recomendacao.objects.all()
    serializer_class = RecomendacaoSerializer

    def get_queryset(self):
        return Recomendacao.objects.filter(usuario=self.request.user)
