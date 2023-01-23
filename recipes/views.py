from django.shortcuts import render

from utils.recipes.factory import make_recipe

# Create your views here.


def home(request):
    # usando list comprehension para preencher multiplas receitas
    # falta implementar no html ainda
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):
    # return render(request, 'recipes/home.html')
    # return render(request, 'recipes/home.html', status=201)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
