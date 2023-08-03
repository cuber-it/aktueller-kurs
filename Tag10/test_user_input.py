import pytest
from unittest.mock import patch
#from user_input_defensiv import get_input
from user_input_offensiv import get_input

def test_get_input_valid():
    with patch('builtins.input', return_value='30'):
        assert get_input() == 30

def test_get_input_invalid():
    with patch('builtins.input', return_value='99'):
        assert get_input() == "Das war nix!"

def test_get_input_invalid_2():
    with patch('builtins.input', return_value='100'):
        assert get_input() == "Das war nix!"

def test_get_input_non_numeric():
    with patch('builtins.input', return_value='hello'):
        assert get_input() == "Das war nix!"
