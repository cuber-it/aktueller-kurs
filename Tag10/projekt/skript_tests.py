import skript
import unittest # oder import pytest
import skript_test_mock as stm

class TestSkript(unittest.TestCase):
    def test_init(self):
        s = skript.Skript(1, 2)
        self.assertEqual(s.a, 1)
        self.assertEqual(s.b, 2)

    def test_get_values(self):
        s = skript.Skript(3, 4)
        self.assertEqual(s.get_values(), (3, 4))

    def test_set_values(self):
        s = skript.Skript(0, 0)
        s.set_values(stm.SourceMock())
        self.assertEqual(s.a, 10)
        self.assertEqual(s.b, 100)

    def test_multiply(self):
        s = skript.Skript(3, 4)
        s.multiply(3, 4)
        self.assertEqual(s.get_values(), (9, 16))

if __name__ == '__main__':
    unittest.main()
