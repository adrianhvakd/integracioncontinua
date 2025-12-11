from app import Calculadora
def test_sumar():
    calc = Calculadora()
    assert calc.sumar(2, 3) == 5
    assert calc.sumar(-1, 1) == 0
    assert calc.sumar(-1, -1) == -2