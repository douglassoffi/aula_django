from recipes.tests.test_recipe_base import RecipeTestBase
from django.urls import reverse, resolve
from recipes.views import *
from unittest.mock import patch

class RecipeCategoryTest(RecipeTestBase):
    def test_category_url(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipe/category/1/')   

    def test_category_view(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, category)

    def test_category_is_200(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertAlmostEqual(response.status_code, 200)

    def test_category_is_404_if_not_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertAlmostEqual(response.status_code, 404)
    
    def test_category_template_used(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertTemplateUsed(response, 'recipes/pages/category.html')

    def test_category_template_loads_recipes(self):
        title = 'category'
        self.make_recipe(title=title)
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')
        self.assertIn(title, content)

    def test_category_template_loads_recipes_if_not_published(self):
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 404)

    @patch('recipes.views.PER_PAGE', new=1)
    def test_category_is_paginated(self):
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
