import unittest
from LottoEngine import check_tipp

class LottoEngineTests(unittest.TestCase):
    def test_checkTipp_all_valid(self):
        tipp = "1,2,3,4,5,6"
        result = check_tipp(tipp.split(","))
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(result, expected)
    
    def test_checkTipp_doubled(self):
        tipp = "1,1,3,4,5,6".split(",")
        with self.assertRaises(Exception) as context:
            check_tipp(tipp)
        self.assertIn("Doubletten im Tipp", str(context.exception))

    def test_checkTipp_invalid_range(self):
        for tipp in ["-1,2,3,4,5,6", "0,2,3,4,5,6", "1,2,3,4,5,50"]:
            with self.assertRaises(Exception) as context:
                check_tipp(tipp.split(","))
            self.assertIn("Ungültiger Feldwert", str(context.exception))

    def test_checkTipp_invalid_length(self):
        for tipp in ["1.2.3.4.5.6", "1,2,3,4,5", "1,2,3,4,5,6,7"]:
            with self.assertRaises(Exception) as context:
                check_tipp(tipp.split(","))
            self.assertIn("Anzahl Felder stimmt nicht", str(context.exception))

    def test_checkTipp_invalid_type(self):
        tipp = "a,2,3,4,5,6".split(",")
        with self.assertRaises(Exception) as context:
            check_tipp(tipp)
        self.assertIn("Ungültiger Feldwert", str(context.exception))

if __name__ == "__main__":
    unittest.main()