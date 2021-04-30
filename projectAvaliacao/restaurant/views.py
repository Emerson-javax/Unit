from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
import json
from .models import Restaurants
from rest_framework.status import HTTP_200_OK
from django.contrib.auth import authenticate, login



# Create your views here.


def index(request):

    restaurant = Restaurants.objects.all()

    contexto = {
        'restaurant': restaurant
    }

    return render(request, "index.html", contexto)



def cadastro(request):

    response = {}

    if request.method == 'POST':

        restaurant = Restaurants()
        restaurant.email = request.POST.get('email')
        restaurant.nome = request.POST.get('nome')
        restaurant.cidade = request.POST.get('cidade')
        restaurant.cpf = request.POST.get('cpf')
        restaurant.save()

        response = {
            'response': HTTP_200_OK
        }

    return HttpResponse(json.dumps(response))


def login(request):

    return render(request, 'login.html')


#######################################


def cardapio(request):

    return render(request, 'cardapio.html')

def carrinho(request):

    return render(request, 'carrinho.html')
