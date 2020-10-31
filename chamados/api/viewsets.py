from rest_framework.viewsets import ModelViewSet

from chamados.models import Chamado, Impressora
from chamados.api.serializers import ChamadoSerializer, ImpressoraSerializer


class ChamadoViewSet(ModelViewSet):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer

    def get_queryset(self):
        return Chamado.objects.filter(impressora__usuario=self.request.user)


class ImpressoraViewSet(ModelViewSet):
    queryset = Impressora.objects.all()
    serializer_class = ImpressoraSerializer

    def get_queryset(self):
        return Impressora.objects.filter(usuario=self.request.user)
