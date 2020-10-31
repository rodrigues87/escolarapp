from django.contrib import admin

# Register your models here.
from chamados.models import Chamado, Impressora


class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('id','titulo', 'descricao','impressora','dataAbertura')


class ImpressoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'status_impressora')


admin.site.register(Chamado, ChamadoAdmin)
admin.site.register(Impressora, ImpressoraAdmin)
