from praktikum.bun import Bun


class TestBun:

    def test_get_name_the_bun_has_a_name(self):
        name_bun = 'Магическая булочка из Хогвартса'
        bun = Bun(name_bun, 4.05)
        assert bun.get_name() == name_bun

    def test_get_price_the_bun_has_a_price(self):
        bun = Bun('Умная булочка', 114.85)
        assert bun.get_price() == 114.85
