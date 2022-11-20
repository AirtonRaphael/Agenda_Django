from django.contrib import admin
from .models import Evento
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criação')
    list_filter = ('usuario',)
admin.site.register(Evento, EventoAdmin)
