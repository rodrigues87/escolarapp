from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from usuarios.api.serializers import UsuariosSerializer
from usuarios.models import User


class UsuariosViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer
    filter_fields = ('email', 'first_name',)

    def get_queryset(self):
        return User.objects.filter(email=self.request.user.email)


@permission_classes([IsAdminUser])
class UsuariosAdmin(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer
    filter_fields = ('first_name',)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
