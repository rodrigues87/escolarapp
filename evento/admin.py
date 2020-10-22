from django.contrib import admin

# Register your models here.
from evento.models import Evento, Favorito

admin.site.register(Evento)
admin.site.register(Favorito)