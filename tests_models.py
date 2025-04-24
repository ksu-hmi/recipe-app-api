import unittest
from recipe_app.models import Recipe

class TestRecipeModel(unittest.TestCase):
    def test_recipe_fields(self):
        r = Recipe(name="Tacos", ingredients="beef, tortilla", instructions="Cook and wrap")
        self.assertEqual(r.name, "Tacos")
