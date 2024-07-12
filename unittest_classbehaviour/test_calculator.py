# test_calculator.py
"""
Testing class behavior using unittest involves verifying that methods and attributes of a class behave 
as expected under different conditions. 
Let's create an example where we have a simple class and then write unittest tests to cover its behavior
"""
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # This method will run before each test method
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
- Class Definition: The Calculator class defines basic arithmetic operations (add, subtract, multiply, 
  divide) and a method (get_result) to retrieve the current result.
- Test Class: TestCalculator is a unittest.TestCase subclass that contains methods (test_add_method, 
  test_subtract_method, etc.) to test different behaviors of the Calculator class.
- setUp Method: setUp method is used to initialize an instance of Calculator (self.calc) before each 
  test method runs, ensuring a clean state for each test.
- Test Methods: Each test method calls various methods of Calculator and asserts that the result is as 
  expected using self.assertEqual.
- Error Handling: test_divide_by_zero_method tests that dividing by zero raises a ValueError.
"""