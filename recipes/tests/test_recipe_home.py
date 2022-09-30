from recipes.tests.test_recipe_base import RecipeTestBase
from django.urls import reverse, resolve
from recipes.views import *

# Precisa ser alterado se arquivo ./recipes/templates/pages/home.html, linha 11 for alterado!
home_no_recipes_message = 'Nenhuma receita encontrada!'

class RecipeHomeTest(RecipeTestBase):
    def test_home_url(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_home_view(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, home)

    def test_home_is_200(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_template_used(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_home_template_used_if_not_found(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(home_no_recipes_message, response.content.decode('utf-8'))

    def test_home_template_loads_recipes(self):
        title = 'home'
        self.make_recipe(title=title)
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        self.assertIn(title, content)

    def test_home_template_loads_recipes_if_not_published(self):
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(home_no_recipes_message, response.content.decode('utf-8'))