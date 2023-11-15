from django.conf import settings
import requests
import json


def get_weather_data(city, country):
	api_key = settings.WEATHER_API_KEY
	url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}'

	response = requests.get(url)

	current_json = json.loads(response)
	weather_data = current_data['current']

	location_name = f"{weather_data['city']['@name']}, {weather_data['city']['country']}"
	temperature = float(weather_data['temperature']['@value'])
    wind_speed = weather_data['wind']['speed']                              
    wind_dir = weather_data['wind']['direction']                          
    cloudiness = weather_data['clouds']['@name']                       
    pressure = weather_data['pressure']['@value']                         
    humidity = weather_data['humidity']['@value']                                  
    
    # Geographical coordinates 
    coord_lat = weather_data['city']['coord']['@lat']                                   
    coord_lon = weather_data['city']['coord']['@lon']                                            
  
    requested_time = weather_data['lastupdate']['@value']                  
    

    # Final formatted data dictionary   
    weather_dict = {
    'location_name': location_name,
    'temperature': f'{temperature}°C',
    'wind': f'{wind_speed} m/s, {wind_dir}',
    'cloudiness': cloudiness,
    'pressure': f'{pressure} hpa',
    'humidity': f'{humidity} %',
    'geo_coordinates': f'[{coord_lat}, {coord_lon}]',
    'requested_time': requested_time
}


    return weather_dict                       
