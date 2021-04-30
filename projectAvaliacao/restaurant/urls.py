from django.urls import path, include
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('index', views.index, name='index'),

    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),

    path('cardapio', views.cardapio, name='cardapio'),
    path('carrinho', views.carrinho, name='carrinho'),
]
