from django.shortcuts import render
from apps.chatbot.models import Sala, Message

def index(request):
    return render(request, 'index.html')

def chat(request):
    salas = Sala.objects.all()
    messages = Message.objects.all()
    
    return render(request, 'chat.html', {
                                        'messages': messages,
                                        'salas': salas,
                                        })

def login(request):
    return render(request, 'user/login.html')

def cadastro(request):
    return render(request, 'user/cadastro.html')