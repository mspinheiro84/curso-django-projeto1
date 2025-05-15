"""Importações."""
from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe
# from django.http import HttpResponse

# Create your views here.


def category(request, category_id):
    """Rota para recipe por category."""
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published = True
    ).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
    })

def home(request):
    recipes = Recipe.objects.filter(
        is_published = True
    ).order_by('-id')
    """Rota para home."""
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def recipes(request, id):
    """Rota para recipes."""
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
