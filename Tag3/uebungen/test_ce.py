#!/usr/bin/env python3
 
import unittest
 
from LottoEngine import check_tipp
 
class TestCheckTipp(unittest.TestCase):
  def test_length_ok(self):
    self.assertEqual(check_tipp([1,2,3,4,5,6]), [1, 2, 3, 4, 5, 6])
 
  def test_raise_count(self):
    self.assertRaises(Exception, check_tipp, [1,2,3,4,5])
 
  def test_raise_value(self):
    self.assertRaises(Exception, check_tipp, [1,2,3,4,5,-6]) # ValueError
 
  def test_raise_double(self):
    self.assertRaises(Exception, check_tipp, [1,2,3,4,5,5])

if __name__ == "__main__":
    unittest.main(verbosity=2)   