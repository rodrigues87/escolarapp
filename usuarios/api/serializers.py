from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from usuarios.models import User
from django.contrib.auth.hashers import make_password


class UsuariosSerializer(ModelSerializer):


    class Meta:
        model = User
        fields = (
            'url', 'username', 'email', 'pk', 'first_name'
        )
