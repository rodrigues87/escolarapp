from rest_framework.viewsets import ModelViewSet
from usuarios.api.serializers import UsuariosSerializer
from usuarios.models import User


class UsuariosViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer
    filter_fields = ('email', 'first_name',)

    def get_queryset(self):
        return User.objects.filter(email=self.request.user.email)
