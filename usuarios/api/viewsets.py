from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from usuarios.api.serializers import UsuariosSerializer
from usuarios.models import User
from rest_framework import viewsets


class UsuariosViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer
    filter_fields = ('email', 'first_name',)


class CurrentUserView(APIView):
    def get(self, request):
        serializer = UsuariosSerializer(request.user)
        return Response(serializer.data)


class CurrentUser(viewsets.ViewSetMixin, generics.ListAPIView):
    serializer_class = UsuariosSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(email=user.email)
