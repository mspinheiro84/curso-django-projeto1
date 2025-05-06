from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('HOME - Recipes')

def contato(request):
    return HttpResponse('Contato - Recipes')

def sobre(request):
    return HttpResponse('Sobre - Recipes')