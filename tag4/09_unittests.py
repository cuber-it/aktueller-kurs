# Tag 4 – Funktionen automatisch prüfen
# unittest bündelt einzelne Prüfungen in einer TestCase-Klasse.
# Start: python3 tag4/09_unittests.py -v

import unittest
from rechner import addiere, teile, ist_gerade


class TestRechner(unittest.TestCase):
    def test_addiere_positive_zahlen(self):
        self.assertEqual(addiere(2, 3), 5)

    def test_addiere_negative_zahlen(self):
        self.assertEqual(addiere(-1, -1), -2)

    def test_addiere_dezimalzahlen(self):
        self.assertAlmostEqual(addiere(0.1, 0.2), 0.3)

    def test_teile_normal(self):
        self.assertEqual(teile(10, 2), 5)

    def test_teile_null_durch_zahl(self):
        self.assertEqual(teile(0, 2), 0)

    def test_teile_durch_null(self):
        with self.assertRaises(ZeroDivisionError):
            teile(5, 0)

    def test_ist_gerade(self):
        for zahl, erwartet in [(4, True), (7, False), (0, True), (-2, True)]:
            with self.subTest(zahl=zahl):
                self.assertEqual(ist_gerade(zahl), erwartet)


if __name__ == "__main__":
    unittest.main()
