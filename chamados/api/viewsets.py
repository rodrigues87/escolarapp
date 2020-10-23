from rest_framework.viewsets import ModelViewSet

from chamados.models import Chamado, Impressora
from chamados.api.serializers import ChamadoSerializer, ImpressoraSerializer


class ChamadoViewSet(ModelViewSet):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer


class ImpressoraViewSet(ModelViewSet):
    queryset = Impressora.objects.all()
    serializer_class = ImpressoraSerializer
