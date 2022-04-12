from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):  # Recipe is the name of the table
    slug = models.SlugField()  # slug is the name of the field
    title = models.CharField(max_length=70)  # title is the name of the column
    description = models.CharField(max_length=200)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=50)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=50)
    preparation_step = models.TextField()
    preparation_step_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/')  # download pillow

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title

# title description slug
# preparation_time preparation_time_unit
# servings servings_unit
# preparation_step
# preparation_step_is_html
# created_at updated_at
# is_published
# cover
# category (relação 1:N)
# author (relação 1:N)
