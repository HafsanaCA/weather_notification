import geocoder
import requests
from odoo import http
from odoo.http import request


class WeatherNotification(http.Controller):
    @http.route('/weather/notification/check', type='json', auth="user", methods=['POST'])
    def weather_notification(self):
        """
        Controller for fetching weather data based on user settings.
        """
        weather_data = {'data': False, 'description': 'No weather data available'}

        if not request.env.user.api_key:
            return {'data': False, 'description': 'API key is not configured.'}
        try:
            if request.env.user.location_set == 'auto':
                g = geocoder.ip('me')
                if g.ok:
                    lat, lng = g.latlng
                    lat = round(lat, 2)
                    lng = round(lng, 2)
                    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={request.env.user.api_key}'
                    response = requests.get(url, timeout=10)
                    print("Detected location from IP:", lat, lng)
                    print("Geocoder response:", g.json)
                    if response.status_code == 200:
                        weather_data = response.json()
                    else:
                        weather_data['description'] = 'Failed to fetch weather data from OpenWeatherMap.'
                else:
                    weather_data['description'] = 'Unable to determine location.'
            elif request.env.user.location_set == 'manual' and request.env.user.city:
                url = f'https://api.openweathermap.org/data/2.5/weather?q={request.env.user.city}&appid={request.env.user.api_key}'
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    weather_data = response.json()
                else:
                    weather_data['description'] = 'Invalid city or API key.'
            else:
                weather_data['description'] = 'City not specified for manual location.'
        except Exception as e:
            weather_data['description'] = f'Error fetching weather data: {str(e)}'
        return weather_data