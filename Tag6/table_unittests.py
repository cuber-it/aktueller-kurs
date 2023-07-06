import table_with_test as table
import unittest
from unittest.mock import Mock

class TestTabelle(unittest.TestCase):

    def setUp(self):
        self.tabelle = table.Tabelle()
        self.tabelle_with_header = table.Tabelle(has_header=True)

    def test_header_count(self):
        self.assertEqual(self.tabelle.header_count(), 0)

    def test_row_count(self):
        self.assertEqual(self.tabelle.row_count(), 0)

    def test_load(self):
        reader = Mock(spec=table.TableReader)
        reader.read.return_value = [[1,2,3], [4,5,6], [7,8,9]]

        self.tabelle.load(reader)
        self.assertEqual(self.tabelle.row_count(), 3)
        self.assertEqual(self.tabelle.header_count(), 0)

    def test_load_with_header(self):
        reader = Mock(spec=table.TableReader)
        reader.read.return_value = [["A", "B", "C"], [4,5,6], [7,8,9]]

        self.tabelle_with_header.load(reader)
        self.assertEqual(self.tabelle_with_header.row_count(), 2)
        self.assertEqual(self.tabelle_with_header.header_count(), 3)

    def test_header_change_fails(self):
        with self.assertRaises(AttributeError):
            self.tabelle.change_header(["X", "Y", "Z"])

    def test_header_change_works(self):
        self.tabelle_with_header.change_header(["X", "Y", "Z"])
        self.assertListEqual(["X", "Y", "Z"], self.tabelle_with_header.header)

    def test_dump(self):
        writer = Mock(spec=table.TableWriter)
        self.tabelle.dump(writer)
        writer.write.assert_called_once()

    def test_load_not_a_TableReader(self):
        with self.assertRaises(TypeError):
            self.tabelle.load("not a TableReader")

    def test_dump_not_a_TableWriter(self):
        with self.assertRaises(TypeError):
            self.tabelle.dump("not a TableWriter")

if __name__ == "__main__":
    unittest.main()
