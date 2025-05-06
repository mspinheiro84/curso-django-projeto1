"""Importações."""
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def home(request):
    """Rota para home."""
    return render(request, 'recipes/home.html', context={
        'name': 'Marcelo Pinheiro',
    })


def contato(request):
    """Rota para contato."""
    return render(request, 'recipes/contato.html')


def sobre(request):
    """Rota para sobre."""
    return render(request, 'recipes/sobre.html')
