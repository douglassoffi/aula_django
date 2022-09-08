from django.test import TestCase
from recipes.models import *

class RecipeTestBase(TestCase):
    def setUp(self) -> None:
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
            title='title',
            description='description',
            slug='slug',
            preparation_time=0,
            preparation_time_unit='preparation_time_unit',
            servings=0,
            servings_unit='servings_unit',
            preparation_steps='preparation_steps',
            preparation_steps_is_html=False,
            is_published=True,
            cover='media/recipes/covers/2022/08/29/lily-banse--YHSwy6uqvk-unsplash.jpg',
        )
        return super().setUp()
