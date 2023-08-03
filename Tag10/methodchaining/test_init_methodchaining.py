import pytest
from init_methodchaining import Daten   # assuming the Daten class is in daten.py

def test_init_werte():
    d = Daten().init_werte(1, 2, 3)
    assert d.values() == ([], [1, 2, 3], [])

    with pytest.raises(AssertionError):
        d.init_werte('a', 'b')

def test_init_texte():
    d = Daten().init_texte('a', 'b')
    assert d.values() == (['a', 'b'], [], [])

    with pytest.raises(AssertionError):
        d.init_texte(1, 2)

def test_init():
    d = Daten().init('a', 1, 'b', 2)
    assert d.values() == (['a', 'b'], [1, 2], [])

    with pytest.raises(TypeError):
        d.init([1, 2, 3], 'a', 'b')

def test_init_float():
    d = Daten().init_float(1.1, 1.2)
    assert d.values() == ([], [], [1.1, 1.2])

    with pytest.raises(AssertionError):
        d.init_float(1, 2)
