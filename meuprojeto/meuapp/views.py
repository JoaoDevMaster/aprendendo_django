# meuapp/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, mundo! Este é o meu primeiro aplicativo Django.")
