import pytest
import klasse

def test_init():
    calc_1 = klasse.Calculator()
    calc_2 = klasse.Calculator(1,2)

    assert str(calc_1) == "0 0 None", f"Mismatch {calc_1}"
    assert str(calc_2) == "1 2 None", f"Mismatch {calc_2}"

def test_add():
    calc = klasse.Calculator()
    result = calc.add()

    assert str(calc) == "0 0 0", f"Mismatch {calc}"
    assert str(result) == "0 0 0", f"Mismatch {result}"
