from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized
from recipes.models import Recipe


class RecipeCategoryModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(
            name='Category Testing'
        )
        return super().setUp()

    def test_recipe_category_string_representation_is_name_field(self):
        self.assertEqual(
            str(self.category),
            self.category.name,
            msg=f'Category string representation must be category name '
                f'"{self.category.name}" but "{str(self.category)}"',
        )

    def test_recipe_category_name_max_length_9s_65_chars(self):
        self.category.name = 'A' * 66
        with self.assertRaises(ValidationError):
            self.category.full_clean()
            self.category.save()
