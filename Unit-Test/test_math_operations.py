import unittest
from math_operations import addition, subtraction

class TestMathOperation(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
    
    def test_addition1(self):
        self.assertNotEqual(addition(3, 5), 7)

    def test_subtraction(self):
        self.assertEqual(subtraction(3, 2), 1)

if __name__ == "__main__":
    unittest.main()
