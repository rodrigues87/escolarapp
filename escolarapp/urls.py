from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from agendamento.api.viewsets import AgendamentoViewSet
from usuarios.api.viewsets import  UsuariosAdmin
from evento.api.viewsets import EventoViewSet, FavoritoViewSet
from chamados.api.viewsets import ChamadoViewSet, ImpressoraViewSet
from remedio.api.viewsets import RemedioViewSet
from tarefas.api.viewsets import TarefeViewSet

from usuarios.views import UserCreateAPIView

router = routers.DefaultRouter()
router.register(r'agendamentos', AgendamentoViewSet)
router.register(r'chamados', ChamadoViewSet)
router.register(r'eventos', EventoViewSet)
router.register(r'favoritos', FavoritoViewSet)
router.register(r'impressoras', ImpressoraViewSet)
router.register(r'lista-usuarios', UsuariosAdmin)
router.register(r'remedios', RemedioViewSet)
router.register(r'tarefas', TarefeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('account/', include('rest_auth.urls')),
    path('account/register/', UserCreateAPIView.as_view()),

]
