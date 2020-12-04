from rest_framework.viewsets import ModelViewSet

from pokemon.models import Pokemon
from pokemon.api.serializers import PokemonSerializer


class PokemonViewSet(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
