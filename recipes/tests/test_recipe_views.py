from django.test import TestCase
from django.urls import reverse, resolve
from recipes.views import *

class RecipeViewsTest(TestCase):
    def test_home_view(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, home)

    def test_category_view(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, category)

    def test_recipe_view(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, recipe)
        
class RecipeViewsStatusCodeTest(TestCase):
    def test_home_view_is_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

class RecipeViewsTemplateTest(TestCase):
    def test_home_view_template_used(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    # Precisa ser alterado se arquivo ./recipes/templates/pages/home.html, linha 11 for alterado!
    def test_home_view_template_used_if_no_recipe(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('Nenhuma receita encontrada!', response.content.decode('utf-8'))