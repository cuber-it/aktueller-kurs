import pytest
import klasse

def test_init_valid():
    calc_1 = klasse.Calculator()
    calc_2 = klasse.Calculator(1,2)

    assert str(calc_1) == "0 0 None", f"Mismatch {calc_1}"
    assert str(calc_2) == "1 2 None", f"Mismatch {calc_2}"

def test_init_invalid():
    with pytest.raises(TypeError):
        calc = klasse.Calculator(3, "a")
    with pytest.raises(TypeError):
        calc = klasse.Calculator("a", 3)
    with pytest.raises(TypeError):
        calc = klasse.Calculator("a", "a")

def test_add():
    calc = klasse.Calculator(3, 5)
    result = calc.add()

    assert str(calc) == "3 5 8", f"Mismatch {calc}"
    assert str(result) == "3 5 8", f"Mismatch {result}"

def test_sub():
    calc = klasse.Calculator(3, 5)
    result = calc.sub()

    assert str(calc) == "3 5 -2", f"Mismatch {calc}"
    assert str(result) == "3 5 -2", f"Mismatch {result}"

def test_mul():
    pass

def test_div():
    calc = klasse.Calculator(4, 2)
    

def test_div_by_zero():
    calc = klasse.Calculator(3, 0)
    with pytest.raises(ZeroDivisionError):
        calc.div()

def test_modulo():
    pass

def test_reset():
    pass

def test_property_wert_a_valid():
    calc = klasse.Calculator(3, 5)
    assert calc.wert_a, 3
    calc.wert_a = 10
    assert str(calc), "10 5 None"

def test_property_wert_a_invalid():
    calc = klasse.Calculator(3, 5)

def test_property_wert_b_valid():
    calc = klasse.Calculator(3, 5)
    assert calc.wert_b, 5
    calc.wert_a = 10
    assert str(calc), "3 10 None"

def test_property_wert_b_invalid():
    calc = klasse.Calculator(3, 5)

def test_property_ergebnis_valid():
    calc = klasse.Calculator(3, 5)

def test_property_ergebnis_invalid():
    calc = klasse.Calculator(3, 5)
