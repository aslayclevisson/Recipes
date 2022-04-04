from django.urls import path

from . import views

app_name = 'recipes' # This is used to namespace the urls. Ex.: recipes:home or recipes:recipe :D

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:pk>/', views.recipe, name='recipe'),
]
