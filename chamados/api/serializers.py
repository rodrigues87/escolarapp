from rest_framework.serializers import ModelSerializer

from chamados.models import Chamado, Impressora


class ChamadoSerializer(ModelSerializer):
    class Meta:
        model = Chamado
        fields = '__all__'
        depth = 1


class ImpressoraSerializer(ModelSerializer):
    class Meta:
        model = Impressora
        fields = '__all__'
