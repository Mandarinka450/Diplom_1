from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase():
    def test_available_buns_get_len_of_buns(self):
        database = Database()
        actual_buns = database.available_buns()

        expected_buns = [
            Bun("black bun", 100),
            Bun("white bun", 200),
            Bun("red bun", 300),
        ]

        assert [(bun.get_name(), bun.get_price()) for bun in actual_buns] == [(bun.get_name(), bun.get_price()) for bun
                                                                              in expected_buns]

    def test_available_ingredients_get_len_of_ingredients(self):
        database = Database()
        actual_ingredients = database.available_ingredients()

        expected_ingredients = [
            Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
            Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300),
        ]

        assert [(ingredient.get_type(), ingredient.get_name(), ingredient.get_price()) for ingredient in
                actual_ingredients] == [(ingredient.get_type(), ingredient.get_name(), ingredient.get_price()) for
                                        ingredient in expected_ingredients]