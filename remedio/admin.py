from django.contrib import admin

# Register your models here.
from remedio.models import Remedio, Recomendacao


class RecomendacaoAdmin(admin.ModelAdmin):
    readonly_fields = ('proximo_horario', 'quantidade_restante', 'quantidade_total_comprimidos',"quantidade_tomada_comprimidos")
    list_display = ('usuario','remedio','intervalo','dias','ultima_hora_que_tomou','quantidade_total_comprimidos','quantidade_restante')


admin.site.register(Remedio)
admin.site.register(Recomendacao, RecomendacaoAdmin)
