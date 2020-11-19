from django import forms
from django.contrib import admin

# Register your models here.
from chamados.models import Chamado, Impressora


class ChamadoRespostaForm(forms.ModelForm):
    resposta = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Chamado
        fields = '__all__'


class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'impressora', 'dataAbertura')
    form = ChamadoRespostaForm


class ImpressoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'status_impressora')


admin.site.register(Chamado, ChamadoAdmin)
admin.site.register(Impressora, ImpressoraAdmin)
