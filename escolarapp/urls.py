from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuarios.api.viewsets import UsuariosViewSet
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views
from usuarios.views import UserCreateAPIView

router = routers.DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('account/register', UserCreateAPIView.as_view())

]
