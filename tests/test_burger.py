from unittest.mock import Mock
import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns_the_burger_has_a_bun(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.configure_mock(name='Булочка из морских водорослей и кунжутом', price=23.45)
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient_add_two_ingredient(self):
        burger = Burger()
        ingredient1_mock = Mock()
        ingredient2_mock = Mock()
        ingredient1_mock.configure_mock(type=INGREDIENT_TYPE_FILLING, nama='Хрустящий сыр', price=187.12)
        ingredient2_mock.configure_mock(type=INGREDIENT_TYPE_FILLING, name='Креветки в кляре', price=324.99)
        burger.add_ingredient(ingredient1_mock)
        burger.add_ingredient(ingredient2_mock)
        assert len(burger.ingredients) == 2

    def test_remove_ingredient_delete_one_ingredient(self):
        burger = Burger()
        ingredient1_mock = Mock()
        ingredient1_mock.configure_mock(type=INGREDIENT_TYPE_FILLING, name='Курочка в кляре', price=100.10)
        burger.add_ingredient(ingredient1_mock)
        burger.remove_ingredient(-1)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_move_ingredient_from_last_index_to_one(self):
        burger = Burger()
        ingredient1_mock = Mock()
        ingredient2_mock = Mock()
        ingredient1_mock.configure_mock(type=INGREDIENT_TYPE_FILLING, name='Свежий салат', price=10.00)
        ingredient2_mock.configure_mock(type=INGREDIENT_TYPE_SAUCE, name='Кетчуп', price=25.00)
        burger.add_ingredient(ingredient1_mock)
        burger.add_ingredient(ingredient2_mock)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient2_mock, ingredient1_mock]

    @pytest.mark.parametrize('price1, price2, price3, total', [
        [20.00, 15.00, 60.00, 115.00],
        [56.90, 34.67, 12.45, 160.92],
        [45.23, 90.00, 110.12, 290.58],
    ])
    def test_get_price_get_correct_calculation_of_final_price(self, price1, price2, price3, total):
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        bun_mock.get_price.return_value = price1
        ingredient1_mock = Mock(spec=Ingredient)
        ingredient2_mock = Mock(spec=Ingredient)
        ingredient1_mock.get_price.return_value = price2
        ingredient2_mock.get_price.return_value = price3
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient1_mock)
        burger.add_ingredient(ingredient2_mock)
        assert burger.get_price() == total

    def test_get_receipt(self):
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        bun_mock.get_name.return_value = 'Булочка из слез'
        bun_mock.get_price.return_value = 5.00
        ingredient_mock = Mock()
        ingredient_mock.get_type.return_value = INGREDIENT_TYPE_FILLING
        ingredient_mock.get_name.return_value = 'Картофельная котлета'
        ingredient_mock.get_price.return_value = 3.00
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert 'Булочка из слез' in burger.get_receipt() and 'Картофельная котлета' in burger.get_receipt() and '13.0' in burger.get_receipt()