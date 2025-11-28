import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalculator()
    
    def test_add(self):
        self.assertEqual(self.calculator.add(5, 3), 8)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(0, 0), 0)
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 4), 6)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)
        self.assertEqual(self.calculator.subtract(0, 5), -5)    
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(7, 6), 42)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)
        self.assertEqual(self.calculator.multiply(0, 100), 0)    
    def test_divide(self):
        self.assertEqual(self.calculator.divide(20, 4), 5)
        self.assertEqual(self.calculator.divide(-9, 3), -3)
        self.assertIsNone(self.calculator.divide(5, 0))
if __name__ == '__main__':
    unittest.main()

