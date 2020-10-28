from rest_framework.viewsets import ModelViewSet

from remedio.api.serializers import RemedioSerializer
from remedio.models import Remedio


class RemedioViewSet(ModelViewSet):
    queryset = Remedio.objects.all()
    serializer_class = RemedioSerializer

    def get_queryset(self):
        return Remedio.objects.filter(usuario=self.request.user)
