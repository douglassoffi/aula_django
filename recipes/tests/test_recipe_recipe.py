from recipes.tests.test_recipe_base import RecipeTestBase
from django.urls import reverse, resolve
from recipes.views import *

class RecipeRecipeTest(RecipeTestBase):
    def test_recipe_url(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipe/1/')

    def test_recipe_view(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, recipe)

    def test_recipe_view_is_200(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertAlmostEqual(response.status_code, 200)

    def test_recipe_is_404_if_not_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertAlmostEqual(response.status_code, 404)

    def test_recipe_is_404_if_not_published(self):
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_template_used(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertTemplateUsed(response, 'recipes/pages/recipe-view.html')

    def test_recipe_template_loads_recipes(self):
        title = 'recipe'
        self.make_recipe(title=title)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')
        self.assertIn(title, content)