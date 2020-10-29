from django.contrib import admin

# Register your models here.
from remedio.models import Remedio,Recomendacao

admin.site.register(Remedio)
admin.site.register(Recomendacao)