from recipes.tests.test_recipe_base import RecipeTestBase
from django.urls import reverse

# Testa se as URLs estão funcionando corretamente

class RecipeURLsTest(RecipeTestBase):
    def test_home_url(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_category_url(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipe/category/1/')        

    def test_recipe_url(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipe/1/')
    