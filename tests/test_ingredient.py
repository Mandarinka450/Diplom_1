from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_get_type_get_sauce_type_of_ingredient(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус из слез и сожалений', 235.00)
        assert ingredient.get_type() == 'SAUCE'

    def test_get_type_get_filling_type_of_ingredient(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Супер пупер супер плюс острый FAT 32', 187.12)
        assert ingredient.get_type() == 'FILLING'

    def test_get_name_the_ingredient_has_a_name(self):
        name_ingredient = 'Острые помидорчики'
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name_ingredient, 56.90)
        assert ingredient.get_name() == name_ingredient

    def test_get_price_the_ingredient_has_a_price(self):
        name_ingredient = 'Мариновые огурчики'
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name_ingredient, 23.70)
        assert ingredient.get_price() == 23.70
