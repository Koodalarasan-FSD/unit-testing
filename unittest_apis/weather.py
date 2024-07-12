# weather.py
import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_weather(self, city):
        url = f'{self.base_url}?q={city}&appid={self.api_key}&units=metric'
        response = requests.get(url)
        
        if response.status_code != 200:
            raise ValueError(f'Failed to fetch weather data: {response.status_code}')

        return response.json()
