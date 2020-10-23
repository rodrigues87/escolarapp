from django.contrib import admin

# Register your models here.
from chamados.models import Chamado,Impressora

admin.site.register(Chamado)
admin.site.register(Impressora)