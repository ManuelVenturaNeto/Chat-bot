from django.contrib import admin
from chatbot.models import Sala, Message

class ListandoSala(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'created_at',)
    list_display_links = ('id', 'user',)
    search_fields = ('user', 'title')
    list_filter = ('user',)
    list_per_page = 10
        
class ListandoMessage(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at',)
    list_display_links = ('id', 'user',)
    search_fields = ('user',)
    list_filter = ('user',)
    list_per_page = 10
    
admin.site.register(Sala, ListandoSala)
admin.site.register(Message, ListandoMessage)