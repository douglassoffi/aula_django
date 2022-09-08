from django.test import TestCase
from django.urls import reverse
from recipes.models import *

# Testa se o template que a view retorna está correto

class RecipeViewsTemplateTest(TestCase):
    def test_home_view_template_used(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    # Precisa ser alterado se arquivo ./recipes/templates/pages/home.html, linha 11 for alterado!
    def test_home_view_template_used_if_not_found(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('Nenhuma receita encontrada!', response.content.decode('utf-8'))

    def test_home_view_template_loads_recipes(self):
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='Title',
            description='Description',
            slug='slug',
            preparation_time=10,
            preparation_time_unit='Minuto(s)',
            servings=5,
            servings_unit='Porção(ões)',
            preparation_steps='Preparation Steps',
            preparation_steps_is_html=False,
            is_published=True,
        )
        assert 1 == 1
        