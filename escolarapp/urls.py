from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuarios.api.viewsets import UsuariosViewSet, CurrentUserView
from evento.api.viewsets import EventoViewSet
from rest_framework.authtoken import views

from usuarios.views import UserCreateAPIView

router = routers.DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('account/', include('rest_auth.urls')),
    path('account/register/', UserCreateAPIView.as_view()),
    path('account/user/', CurrentUserView),


]
