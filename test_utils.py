from utils import sumar, restar


def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(2, 2) == 4
    assert sumar(1, 1) == 2


def test_restar():
    assert restar(2, 1) == 1
    assert restar(4, 2) == 2
    assert restar(5, 5) == 0
