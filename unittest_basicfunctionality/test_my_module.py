# test_my_module.py

# simple example of using Python's built-in unittest framework to write and run tests for a Python program

import unittest
from my_module import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_add_numbers(self):
        result = add_numbers(3, 5)
        self.assertEqual(result, 8)  # Assert that the result is equal to 8

    def test_add_numbers_negative(self):
        result = add_numbers(-3, 5)
        self.assertEqual(result, 2)  # Assert that the result is equal to 2

    def test_add_numbers_zero(self):
        result = add_numbers(0, 0)
        self.assertEqual(result, 0)  # Assert that the result is equal to 0

if __name__ == '__main__':
    unittest.main()

"""
- We import unittest and the add_numbers function from my_module.
- We define a test class TestAddNumbers that inherits from unittest.TestCase.
- Inside this class, we define individual test methods (test_add_numbers, test_add_numbers_negative, 
  test_add_numbers_zero), each of which tests different scenarios of the add_numbers function using 
  assertions provided by unittest.TestCase.
- unittest.main() runs all the test methods in the script when executed directly.
"""
