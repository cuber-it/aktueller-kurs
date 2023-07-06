import unittest
import klasse

class TestTabelle(unittest.TestCase):

    def test_init(self):
        calc_1 = klasse.Calculator()
        calc_2 = klasse.Calculator(1,2)

        self.assertEqual(calc_1.__str__(), "0 0 None", msg = f"Mismatch {calc_1}")
        self.assertEqual(calc_2.__str__(), "1 2 None", msg = f"Mismatch {calc_2}")

    def test_add(self):
        calc = klasse.Calculator()
        result = calc.add()
        self.assertEqual(calc.__str__(), "0 0 0", msg = f"Mismatch {calc}")
        self.assertEqual(result.__str__(), "0 0 0", msg = f"Mismatch {result}")

if __name__ == "__main__":
    unittest.main()
