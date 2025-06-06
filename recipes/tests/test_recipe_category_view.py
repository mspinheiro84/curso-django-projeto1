from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase
from unittest import skip


class RecipeCategoryViewsTest(RecipeTestBase):
    def tearDown(self) -> None:
        return super().tearDown()

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', args=(1,))
        )
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', args=(1000,))
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category test'
        # Need a recipe or this test
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        # Check if one recipe exists
        self.assertIn(needed_title, content)

    def test_recipe_category_template_dont_loads_recipes_not_publish(self):
        """test recipe is_published False dont show"""
        # Need a recipe or this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:category', args=(recipe.category.id,)))

        self.assertEqual(response.status_code, 404)
