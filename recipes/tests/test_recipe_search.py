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

    def test_search_can_find_by_title(self):
        title1 = 'title 1'
        title2 = 'title 2'

        recipe1 = self.make_recipe(
            slug='1', title=title1, author={'username': '1'}
        )
        recipe2 = self.make_recipe(
            slug='2', title=title2, author={'username': '2'}
        )

        search_url = reverse('recipes:search')
        response1 = self.client.get(f'{search_url}?q={title1}')
        response2 = self.client.get(f'{search_url}?q={title2}')
        response_both = self.client.get(f'{search_url}?q=title')

        self.assertIn(recipe1, response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])

        self.assertIn(recipe2, response2.context['recipes'])
        self.assertNotIn(recipe1, response2.context['recipes'])

        self.assertIn(recipe1, response_both.context['recipes'])
        self.assertIn(recipe2, response_both.context['recipes'])
