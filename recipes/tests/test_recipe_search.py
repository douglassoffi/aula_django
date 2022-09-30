from recipes.tests.test_recipe_base import RecipeTestBase
from django.urls import reverse, resolve
from recipes.views import *

class RecipeSearchTest(RecipeTestBase):
    def test_search_url(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipe/search/')

    def test_search_view(self):
        view = resolve(reverse('recipes:search'))
        self.assertIs(view.func, search)

    def test_search_is_404_if_no_term(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code, 404)

    def test_search_template_used(self):
        response = self.client.get(reverse('recipes:search') + '?q=test')
        self.assertTemplateUsed(response, 'recipes/pages/search-view.html')

    def test_search_term_is_escaped(self):
        response = self.client.get(reverse('recipes:search') + '?q=<test>')
        self.assertIn('&quot;&lt;test&gt;&quot;', response.content.decode('utf-8'))  
