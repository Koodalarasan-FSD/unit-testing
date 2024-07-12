# test_weather.py
import unittest
import requests
from unittest.mock import patch, MagicMock
from weather import WeatherAPI

"""
Testing APIs and external services using unittest involves verifying that your code correctly interacts 
with external endpoints, handles responses, and processes data as expected. Let's create an example 
where we have a Python module that interacts with an external API, and then write unittest tests to 
cover its functionality
"""

class TestWeatherAPI(unittest.TestCase):

    @patch('requests.get')
    def test_get_weather_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'main': {'temp': 20.0},
            'weather': [{'description': 'Cloudy'}]
        }
        mock_get.return_value = mock_response

        weather_api = WeatherAPI(api_key='fake_api_key')
        weather_data = weather_api.get_weather('London')

        self.assertEqual(weather_data['main']['temp'], 20.0)
        self.assertEqual(weather_data['weather'][0]['description'], 'Cloudy')

    @patch('requests.get')
    def test_get_weather_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        weather_api = WeatherAPI(api_key='fake_api_key')

        with self.assertRaises(ValueError):
            weather_api.get_weather('London')

if __name__ == '__main__':
    unittest.main()

"""
- Module Definition: weather.py defines a WeatherAPI class that interacts with an external weather 
  API (api.openweathermap.org).

- Test Class: TestWeatherAPI is a unittest.TestCase subclass that contains methods 
  (test_get_weather_success, test_get_weather_failure) to test the interaction with WeatherAPI class.

- Mocking Requests: @patch('requests.get') decorator is used to mock the requests.get function, ensuring 
  that actual API calls are not made during testing.

- Mock Response: MagicMock is used to simulate API responses (mock_response) with different status 
  codes (200 for success, 404 for failure) and JSON data.

- Test Methods:

    - test_get_weather_success: Tests that get_weather method correctly handles a successful API 
      response and parses the expected weather data.
    - test_get_weather_failure: Tests that get_weather method raises a ValueError when the API returns 
      a non-200 status code.
- Running the Tests: Save all files (weather.py, test_weather.py) in the same directory. 
  To run the tests, execute python test_weather.py in your terminal or command prompt. 
  This will execute all defined test methods and report whether each test passed or failed, ensuring 
  that your code correctly interacts with the external weather API.

These tests ensure that your code correctly handles interactions with external APIs, validates 
responses, and processes data as expected, enhancing reliability and robustness of your application 
when dealing with external services. Adjust and expand these examples as needed for more complex API 
interactions or additional functionalities.
"""