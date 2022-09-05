from django.test import TestCase
from django.urls import reverse, resolve
from recipes.views import *

class RecipeViewsTest(TestCase):
    def test_home_view_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, home)

    def test_category_view_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, category)

    def test_recipe_view_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, recipe)
        