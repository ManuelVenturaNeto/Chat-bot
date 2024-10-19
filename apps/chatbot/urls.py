from django.urls import path
from apps.chatbot.views import index, login, cadastro, chat

urlpatterns = [
    path('', index, name='index'),
    path('chat/', chat, name='chat'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
]
