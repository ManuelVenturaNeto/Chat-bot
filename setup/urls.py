from django.contrib import admin
from django.urls import path
from chatbot.views import index, login, cadastro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('', login, name='login'),
    path('', cadastro, name='cadastro'),
]
