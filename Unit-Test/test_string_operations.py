import unittest
from string_operations import reverse_string

class TestStringOperation(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertNotEqual(reverse_string("madam"), "madam")

if __name__ == "__main__":
    unittest.main()