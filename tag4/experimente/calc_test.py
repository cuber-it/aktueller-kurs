import unittest
from calc import addiere, subtrahiere, multipliziere, dividiere


class TestCalc(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_addiere(self):
        self.assertEqual(addiere(3, 5), 8)

    def test_subtrahiere(self):
        self.assertEqual(subtrahiere(10, 4), 6)

    def test_multipliziere(self):
        self.assertEqual(multipliziere(3, 4), 12)

    def test_dividiere(self):
        self.assertEqual(dividiere(1, 2), 0.5)

    def test_dividiere_null(self):
        self.assertEqual(dividiere(0, 2), 0.0)

    def test_dividiere_durch_null(self):
        with self.assertRaises(ZeroDivisionError):
            dividiere(1, 0)

if __name__ == "__main__":
    unittest.main()
