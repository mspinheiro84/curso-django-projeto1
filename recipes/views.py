"""Importações."""
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def home(request):
    """Rota para home."""
    return render(request, 'recipes/home.html')


def contato(request):
    """Rota para contato."""
    return render(request, 'recipes/contato.html', context={
        'name': 'Marcelo Pinheiro',
    })
