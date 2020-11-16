from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from chamados.models import Chamado, Impressora


class ChamadoSerializer(ModelSerializer):
    class Meta:
        model = Chamado
        fields = '__all__'


class ImpressoraSerializer(ModelSerializer):
    class Meta:
        model = Impressora
        fields = '__all__'
