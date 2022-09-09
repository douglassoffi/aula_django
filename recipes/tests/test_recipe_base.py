from django.test import TestCase
from recipes.models import *

class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_author(
        self,
        first_name='first_name',
        last_name='last_name',
        username='username',
        password='password',
        email='email',
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_category(
        self, 
        name='name'
    ):
        return Category.objects.create(name=name)
    
    def make_recipe(
        self,
        category=None,
        author=None,
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
    ):
        if category is None:
            category = {}

        if author is None:
            author = {}

        return Recipe.objects.create(
            category=self.make_category(**category),
            author=self.make_author(**author),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
            cover='media/recipes/covers/2022/08/29/lily-banse--YHSwy6uqvk-unsplash.jpg',
        )
