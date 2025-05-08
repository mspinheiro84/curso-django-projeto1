"""Importações."""
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def home(request):
    """Rota para home."""
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Marcelo Pinheiro',
    })


def recipes(request, id):
    """Rota para home."""
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Marcelo Pinheiro',
    })
