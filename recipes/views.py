from django.shortcuts import render
from utils.recipe.yard import make_recipe

from recipes.models import Recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={'recipes': recipes})

def recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if recipe.is_published is not True:
        pass
    
    return render(request, 'recipes/pages/recipe.html', context={
        'recipe': recipe, 'is_detail_page': True,})
    
def category(request, category_id):
    recipes = Recipe.objects.filter(is_published=True, category__id=category_id).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={'recipes': recipes})
