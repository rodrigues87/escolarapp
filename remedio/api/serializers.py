from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer,StringRelatedField

from remedio.models import Remedio, Recomendacao


class RemedioSerializer(ModelSerializer):
    class Meta:
        model = Remedio
        fields = '__all__'


class RecomendacaoSerializer(ModelSerializer):

    class Meta:
        model = Recomendacao
        fields = 'id','qnt_comprimidos','intervalo','horario_inicial','dose','remedio'
        depth = 1
