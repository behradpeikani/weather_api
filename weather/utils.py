from django.conf import settings
import requests
import json
from ninja.errors import HttpError


def get_weather_data(city, country):
	api_key = settings.WEATHER_API_KEY
	url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric'

	response = requests.get(url)

	if response.status_code == 503:
            raise HttpError(503, "OpenWeatherMap API is currently unavailable. Please try again later.")
	elif response.status_code == 200:
		weather_data = response.json()

	temp_min = weather_data['main']['temp_min']
	temp_max = weather_data['main']['temp_max']
	wind_speed = weather_data['wind']['speed']                                                                               
	pressure = weather_data['main']['pressure']                         
	humidity = weather_data['main']['humidity']                                  
	
	# Geographical coordinates 
	coord_lat = weather_data['coord']['lat']                                   
	coord_lon = weather_data['coord']['lon']                                                             
	

	# Final formatted data dictionary   
	weather_dict = {
	'min_temperature': f'{temp_min}°C',
	'max_temperature': f'{temp_max}°C',
	'wind_speed': f'{wind_speed} m/s',
	'pressure': f'{pressure} hPa',
	'humidity': f'{humidity} %',
	'coord_lat': f'{coord_lat}',
	'coord_lon': f'{coord_lon}',
}


	return weather_dict                       
