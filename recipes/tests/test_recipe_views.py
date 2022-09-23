from recipes.tests.test_recipe_base import RecipeTestBase
from django.urls import reverse, resolve
from recipes.views import *

# Testa se a view utilizada é a correta

class RecipeViewsTest(RecipeTestBase):
    def test_home_view(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, home)

    def test_category_view(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, category)

    def test_recipe_view(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, recipe)

    def test_search_view(self):
        view = resolve(reverse('recipes:search'))
        self.assertIs(view.func, search)
