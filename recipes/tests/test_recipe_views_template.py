from recipes.tests.test_recipe_base import RecipeTestBase
from django.urls import reverse
from recipes.models import *

# Testa se o template que a view retorna está correto

class RecipeViewsTemplateTest(RecipeTestBase):
    def test_home_view_template_used(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    # Precisa ser alterado se arquivo ./recipes/templates/pages/home.html, linha 11 for alterado!
    def test_home_view_template_used_if_not_found(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('Nenhuma receita encontrada!', response.content.decode('utf-8'))

    def test_home_view_template_loads_recipes(self):
        self.make_recipe(
            title='title',
            )
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        context = response.context['recipes']
        self.assertIn('title', content)
        self.assertEqual(len(context), 1)
