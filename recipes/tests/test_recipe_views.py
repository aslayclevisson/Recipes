import email

from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views
from recipes.models import Category, Recipe, User


class ViewsTest(TestCase):
    def test_recipe_home_views_function(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_recipe_views_function(self):
        view = resolve(reverse('recipes:recipe', kwargs={'pk': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_category_views_function(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_home_status_code_is_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_load_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_has_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('recipes', response.context)  # o context retorna uma lista com palavras # noqa: E501

    def test_recipe_category_view_return_404_if_category_not_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 10000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_return_404_if_recipe_not_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'pk': 10000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_template_loads_with_correct_context(self):
        category = Category.objects.create(name='Category U')
        author = User.objects.create(
            first_name='user1',
            last_name='user2',
            username='user3',
            password='user4',
            email='4sl4y@gmail.com')

        recipe = Recipe.objects.create(
            slug='recipe-title',
            title='Recipe Title',
            description='Recipe Description',
            preparation_time=10,
            preparation_time_unit='min',
            servings=2,
            servings_unit='pessoa',
            preparation_step='Preparation Step',
            preparation_step_is_html=False,
            created_at='2020-01-01',
            updated_at='2020-01-01',
            is_published=True,
            cover=None,

            category=category,
            author=author
        )
        ...
