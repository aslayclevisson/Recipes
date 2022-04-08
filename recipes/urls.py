from django.urls import path

from . import views

# This is used to namespace the urls. Ex.: recipes:home or recipes:recipe :D
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/category/<int:category_id>/',
         views.category, name='category'),
    path('recipes/<int:pk>/', views.recipe, name='recipe'),
]
