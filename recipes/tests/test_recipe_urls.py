from django.test import TestCase
from django.urls import reverse


class URLTests(TestCase):
    def test_home_url_page(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')
        self.assertEqual(self.client.get('/').status_code, 200)

    def test_recipe_url_detail_page(self):
        url = reverse('recipes:recipe', kwargs={'pk': 1})
        self.assertEqual(url, '/recipes/1/')
        # self.assertEqual(self.client.get('/recipes/1/').status_code, 200)

    def test_recipe_url_category_page(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')
        # self.assertEqual(self.client.get('recipes/category/1/').status_code, 200) # noqa
