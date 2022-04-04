from django.shortcuts import render
from utils.recipe.yard import make_recipe


# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', context={'recipes':[make_recipe() for _ in range(8)]})

def recipe(request):
    return render(request, 'recipes/pages/recipe.html', context={
        'recipe': make_recipe(),
    })

