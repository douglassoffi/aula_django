from recipes.tests.test_recipe_base import RecipeTestBase
from django.urls import reverse
from recipes.models import *

# Testa se o template que a view retorna está correto
# Precisa ser alterado se arquivo ./recipes/templates/pages/home.html, linha 11 for alterado!
home_no_recipes_message = 'Nenhuma receita encontrada!'

class RecipeViewsTemplateTest(RecipeTestBase):
    def test_home_view_template_used(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_home_view_template_used_if_not_found(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(home_no_recipes_message, response.content.decode('utf-8'))

    def test_home_view_template_loads_recipes(self):
        title = 'home'
        self.make_recipe(title=title)
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        self.assertIn(title, content)

    def test_home_view_template_loads_recipes_if_not_published(self):
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(home_no_recipes_message, response.content.decode('utf-8'))

    def test_category_view_template_used(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertTemplateUsed(response, 'recipes/pages/category.html')

    def test_category_view_template_loads_recipes(self):
        title = 'category'
        self.make_recipe(title=title)
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')
        self.assertIn(title, content)

    def test_recipe_view_template_used(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertTemplateUsed(response, 'recipes/pages/recipe-view.html')

    def test_recipe_view_template_loads_recipes(self):
        title = 'recipe'
        self.make_recipe(title=title)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')
        self.assertIn(title, content)

    def test_search_view_template_used(self):
        response = self.client.get(reverse('recipes:search') + '?q=test')
        self.assertTemplateUsed(response, 'recipes/pages/search-view.html')

    def test_search_term_is_escaped(self):
        response = self.client.get(reverse('recipes:search') + '?q=<test>')
        self.assertIn('&quot;&lt;test&gt;&quot;', response.content.decode('utf-8'))      
