from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from usuarios.api.serializers import UsuariosSerializer
from usuarios.models import User


class UsuariosViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UsuariosSerializer
    filter_fields = ('email',)


class CurrentUserView(APIView):
    def get(self, request):
        serializer = UsuariosSerializer(request.user)
        return Response(serializer.data)
