# test_traffic_light.py
import unittest
from traffic_light import TrafficLight\

"""
Testing state management typically involves verifying that your application maintains and updates its 
internal state correctly across various operations and interactions. This can include testing state 
changes, transitions, and ensuring consistency in different scenarios. Let's create an example where we 
have a simple state management class, and then write unittest tests to cover its functionality:
"""

class TestTrafficLight(unittest.TestCase):

    def setUp(self):
        self.traffic_light = TrafficLight()

    def test_initial_state(self):
        self.assertEqual(self.traffic_light.get_current_state(), 'red')

    def test_change_to_green(self):
        self.traffic_light.change_to_green()
        self.assertEqual(self.traffic_light.get_current_state(), 'green')

    def test_change_to_yellow(self):
        # Test invalid transition (should remain red)
        self.traffic_light.change_to_yellow()
        self.assertEqual(self.traffic_light.get_current_state(), 'red')

        # Test valid transition (from green to yellow)
        self.traffic_light.change_to_green()
        self.traffic_light.change_to_yellow()
        self.assertEqual(self.traffic_light.get_current_state(), 'yellow')

    def test_change_to_red(self):
        # Test invalid transition (should remain yellow)
        self.traffic_light.change_to_red()
        self.assertEqual(self.traffic_light.get_current_state(), 'red')

        # Test valid transition (from yellow to red)
        self.traffic_light.change_to_green()
        self.traffic_light.change_to_yellow()
        self.traffic_light.change_to_red()
        self.assertEqual(self.traffic_light.get_current_state(), 'red')

if __name__ == '__main__':
    unittest.main()

"""
- Class Definition: TrafficLight class defines state management for a traffic light with methods 
  (change_to_green, change_to_yellow, change_to_red) to transition between states ('red', 'green', 'yellow').

- Test Class: TestTrafficLight is a unittest.TestCase subclass that contains methods 
  (test_initial_state, test_change_to_green, test_change_to_yellow, test_change_to_red) to test 
  state management functionality.

- setUp Method: setUp method initializes a new TrafficLight instance (self.traffic_light) before each 
  test method runs, ensuring a clean initial state for each test.

- Test Methods:

    - test_initial_state: Tests that the initial state of TrafficLight is 'red'.
    - test_change_to_green, test_change_to_yellow, test_change_to_red: Tests state transitions between 
    'red', 'green', 'yellow', and back to 'red'.
    - Includes tests for both valid and invalid state transitions to ensure state changes are handled 
      correctly.
- Running the Tests: Save all files (traffic_light.py, test_traffic_light.py) in the same directory. 
  To run the tests, execute python test_traffic_light.py in your terminal or command prompt. 
  This will execute all defined test methods and report whether each test passed or failed, ensuring 
  that your state management logic functions correctly across different transitions and scenarios.

These tests ensure that the TrafficLight class maintains its state correctly and handles state 
transitions according to its defined behavior. Adjust and expand these examples as needed for more 
complex state management scenarios or additional functionalities in your application.
"""