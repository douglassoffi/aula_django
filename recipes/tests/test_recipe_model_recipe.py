from recipes.tests.test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized

class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defaults(self):
        recipe = Recipe(
            category=self.make_category(name='category2'),
            author=self.make_author(username='author2'),
            title='title',
            description='description',
            slug='slug',
            preparation_time=0,
            preparation_time_unit='preparation_time_unit',
            servings=0,
            servings_unit='servings_unit',
            preparation_steps='preparation_steps',
            cover='media/recipes/covers/2022/08/29/lily-banse--YHSwy6uqvk-unsplash.jpg',
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    @parameterized.expand([
            ('title', 50),
            ('description', 150),
            ('preparation_time_unit', 50),
            ('servings_unit', 50)
        ])
    def test_field_max_length(self, field, max_length):
            setattr(self.recipe, field, 'A' * (max_length + 1))
            with self.assertRaises(ValidationError):
                self.recipe.full_clean()

    def test_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.preparation_steps_is_html,
        )

    def test_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.is_published,
        )

    def test_string_representation(self):
        title = 'title'
        self.assertEqual(str(self.recipe), title)
