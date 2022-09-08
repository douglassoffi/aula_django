from recipes.tests.test_recipe_base import RecipeTestBase
from django.urls import reverse

# Teste se status code da view está correto

class RecipeViewsStatusCodeTest(RecipeTestBase):
    def test_home_view_is_200(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_category_view_is_200(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertAlmostEqual(response.status_code, 200)

    def test_category_view_is_404_if_not_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 9999}))
        self.assertAlmostEqual(response.status_code, 404)

    def test_recipe_view_is_200(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertAlmostEqual(response.status_code, 200)

    def test_recipe_view_is_404_if_not_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 9999}))
        self.assertAlmostEqual(response.status_code, 404)
