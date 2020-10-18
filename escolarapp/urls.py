from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuarios.api.viewsets import UsuariosViewSet
from rest_framework.authtoken import views

from usuarios.views import UserCreateAPIView

router = routers.DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),


    path('rest_auth/', include('rest_auth.urls')),
    path('rest_auth/registration/', include('rest_auth.registration.urls'))
]
