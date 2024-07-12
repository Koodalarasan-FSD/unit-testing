# test_math_operations.py

"""
let's delve into testing edge cases using unittest. Edge cases are scenarios that test the extreme or 
boundary conditions of your code, ensuring that it behaves correctly even under unusual or challenging 
inputs. 
"""
import unittest
from math_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        # Normal case
        self.assertEqual(add(3, 5), 8)

        # Edge case: Adding zero
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 0), 0)

        # Edge case: Adding negative numbers
        self.assertEqual(add(-3, 5), 2)
        self.assertEqual(add(3, -5), -2)
        self.assertEqual(add(-3, -5), -8)

    def test_subtract(self):
        # Normal case
        self.assertEqual(subtract(10, 3), 7)

        # Edge case: Subtracting zero
        self.assertEqual(subtract(10, 0), 10)
        self.assertEqual(subtract(0, 0), 0)

        # Edge case: Subtracting negative numbers
        self.assertEqual(subtract(-3, 5), -8)
        self.assertEqual(subtract(3, -5), 8)
        self.assertEqual(subtract(-3, -5), 2)

    def test_multiply(self):
        # Normal case
        self.assertEqual(multiply(4, 6), 24)

        # Edge case: Multiplying by zero
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 0), 0)

        # Edge case: Multiplying negative numbers
        self.assertEqual(multiply(-4, 6), -24)
        self.assertEqual(multiply(4, -6), -24)
        self.assertEqual(multiply(-4, -6), 24)

    def test_divide(self):
        # Normal case
        self.assertEqual(divide(10, 2), 5)

        # Edge case: Dividing by zero
        with self.assertRaises(ValueError):
            divide(10, 0)

        # Edge case: Dividing zero by a number
        self.assertEqual(divide(0, 5), 0)

        # Edge case: Dividing negative numbers
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)

if __name__ == '__main__':
    unittest.main()

"""
- Each test method (test_add, test_subtract, test_multiply, test_divide) within TestMathOperations class 
  tests both normal and edge cases for the corresponding functions (add, subtract, multiply, divide).
- Normal cases ensure that functions behave as expected under typical conditions.
- Edge cases explore scenarios such as adding or subtracting zero, handling negative numbers, dividing 
  by zero, and other extreme conditions.
- self.assertEqual assertions verify that the actual output matches the expected output for each scenario.
"""