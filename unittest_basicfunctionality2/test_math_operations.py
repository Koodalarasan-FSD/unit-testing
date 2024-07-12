# test_math_operations.py
import unittest
from math_operations import add, subtract, multiply, divide, Calculator

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_subtract(self):
        result = subtract(10, 3)
        self.assertEqual(result, 7)

    def test_multiply(self):
        result = multiply(4, 6)
        self.assertEqual(result, 24)

    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_method(self):
        self.calc.add(3)
        self.assertEqual(self.calc.get_result(), 3)

    def test_subtract_method(self):
        self.calc.add(10)
        self.calc.subtract(5)
        self.assertEqual(self.calc.get_result(), 5)

    def test_multiply_method(self):
        self.calc.add(2)
        self.calc.multiply(3)
        self.assertEqual(self.calc.get_result(), 6)

    def test_divide_method(self):
        self.calc.add(10)
        self.calc.divide(2)
        self.assertEqual(self.calc.get_result(), 5)

    def test_divide_by_zero_method(self):
        with self.assertRaises(ValueError):
            self.calc.divide(0)

if __name__ == '__main__':
    unittest.main()

"""
- The math_operations.py module includes functions (add, subtract, multiply, divide) and a 
  class (Calculator) with methods (add, subtract, multiply, divide, get_result).
- The test_math_operations.py script uses unittest to test these functions and the Calculator class.
- Test methods (test_add, test_subtract, etc.) are defined within TestMathOperations and TestCalculator 
  classes, each inheriting from unittest.TestCase.
- Assertions like self.assertEqual are used to verify expected results against actual results from 
  function calls or method invocations.
- The setUp method in TestCalculator initializes a Calculator instance before each test method runs.
"""