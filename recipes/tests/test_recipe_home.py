from recipes.tests.test_recipe_base import RecipeTestBase
from django.urls import reverse, resolve
from recipes.views import *
from unittest.mock import patch

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

    @patch('recipes.views.PER_PAGE', new=1)
    def test_home_is_paginated(self):
        for i in range(3):
            kwargs = {
                'slug':f'slug-{i}',
                'author':{
                    'username':f'username-{i}'
                }
            }
            self.make_recipe(**kwargs)
        response = self.client.get(reverse('recipes:home'))
        recipes = response.context['recipes']
        paginator = recipes.paginator
        self.assertEqual(paginator.num_pages, 3)
        self.assertEqual(len(paginator.get_page(1)), 1)
        self.assertEqual(len(paginator.get_page(2)), 1)
        self.assertEqual(len(paginator.get_page(3)), 1)
