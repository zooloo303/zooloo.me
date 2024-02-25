from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_bot, name='chat_bot'),
    path('getResponse/', views.getResponse, name='getResponse'),
]