"""Importações."""
from django.shortcuts import render
from utils.recipes.factory import make_recipe
# from django.http import HttpResponse

# Create your views here.


def home(request):
    """Rota para home."""
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipes(request, id):
    """Rota para home."""
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
