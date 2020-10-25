from rest_framework.serializers import ModelSerializer

from remedio.models import Remedio


class RemedioSerializer(ModelSerializer):
    class Meta:
        model = Remedio
        fields = '__all__'
