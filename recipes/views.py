# from utils.recipe.yard import make_recipe

from django.shortcuts import get_list_or_404, get_object_or_404, render

from recipes.models import Recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html',
                  context={'recipes': recipes})


def recipe(request, pk):
    recipe = get_object_or_404(Recipe.objects.filter(pk=pk,
                                                     is_published=True))

    return render(request, 'recipes/pages/recipe.html',
                  context={'recipe': recipe,
                           'is_detail_page': True, })


def category(request, category_id):
    # para usar o get list com filtro e order by, melhor usar a query completa como abaixo. # noqa: E501
    recipes = get_list_or_404(
        Recipe.objects.filter(
            is_published=True,
            category__id=category_id
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html',
                  context={'recipes': recipes,
                           'title': f'Category - {recipes[0].category.name}',
                           })
