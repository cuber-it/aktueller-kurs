"""Referenzlösung: Den vereinbarten Funktionsvertrag mit unittest prüfen."""

import unittest
from .statistik import statistik


class TestStatistik(unittest.TestCase):
    def test_positive_werte(self):
        self.assertEqual(statistik(7, 2, 9, 4), (2, 9, 5.5))

    def test_negative_werte(self):
        self.assertEqual(statistik(-7, -2, -9, -4), (-9, -2, -5.5))

    def test_einzelner_wert(self):
        self.assertEqual(statistik(42), (42, 42, 42))

    def test_gemischte_vorzeichen(self):
        self.assertEqual(statistik(-1, 0, 1), (-1, 1, 0))

    def test_dezimalzahlen(self):
        kleinste, groesste, mittelwert = statistik(0.1, 0.2)
        self.assertEqual((kleinste, groesste), (0.1, 0.2))
        self.assertAlmostEqual(mittelwert, 0.15)

    def test_keine_werte(self):
        with self.assertRaises(ValueError):
            statistik()

    def test_liste_entpacken(self):
        werte = [1, 3, 5]
        self.assertEqual(statistik(*werte), (1, 5, 3))


if __name__ == "__main__":
    unittest.main()
