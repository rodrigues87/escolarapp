from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, StringRelatedField

from remedio.models import Remedio, Recomendacao


class RemedioSerializer(ModelSerializer):
    class Meta:
        model = Remedio
        fields = '__all__'


class RecomendacaoSerializer(ModelSerializer):
    class Meta:
        model = Recomendacao
        read_only_fields = "quantidade_total_comprimidos", \
                           "quantidade_tomada_comprimidos", \
                           "quantidade_restante", \
                           "proximo_horario", \
                           "remedio", \
                           "intervalo", \
                           "dias", "proximo_horario",\
                           "usuario"
        fields = '__all__'
