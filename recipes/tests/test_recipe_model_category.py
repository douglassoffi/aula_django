from recipes.tests.test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized

class CategoryModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category()
        return super().setUp()

    @parameterized.expand([
            ('name', 50)
        ])
    def test_field_max_length(self, field, max_length):
            setattr(self.category, field, 'A' * (max_length + 1))
            with self.assertRaises(ValidationError):
                self.category.full_clean()

    def test_category_representation(self):
        self.assertEqual(str(self.category), self.category.name)