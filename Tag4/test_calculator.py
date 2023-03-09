import unittest


from calculator import Calc, CalcException


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calc(0,0)

    def test_add_both_int(self):
        # Test adding positive integers
        self.calc.set(-2, 3)
        self.calc.add()
        self.assertEqual(self.calc.get_result(), 1)

    def test_add_both_float(self):
        # Test adding negative integers
        self.calc.set(-2.1, 3.8)
        self.calc.add()
        self.assertEqual(self.calc.get_result(), 1.7)

    def test_add_both_char(self):
        # Test adding zero
        self.assertRaises(CalcException, self.calc.set, "a", "b")


    def test_reset(self):
        self.calc.set(2, 3)
        self.calc.add()
        self.calc.reset()
        self.assertIsNone(self.calc.get_result())

if __name__ == "__main__":
    unittest.main()
