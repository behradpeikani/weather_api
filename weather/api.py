from ninja import Router
from .schemas import WeatherInSchema, WeatherOutSchema
from .utils import get_weather_data  
from ninja.errors import HttpError
from ninja.security import django_auth

weather_router = Router()

@weather_router.post("/weather", response={200: WeatherOutSchema}, auth=django_auth)
def post_weather(request, payload: WeatherInSchema):
    """
    Retrieve weather data based on provided city and country.
    """
    city = payload.city
    country = payload.country


    try:
        # Fetch weather data using the provided city and country
        weather_data = get_weather_data(city, country)

        # Format the fetched weather data into WeatherOutSchema
        formatted_weather_data = WeatherOutSchema(
            min_temperature=weather_data['min_temperature'],
            max_temperature=weather_data['max_temperature'],
            wind_speed=weather_data['wind_speed'],
            pressure=weather_data['pressure'],
            humidity=weather_data['humidity'],
            coord_lat=weather_data['coord_lat'],
            coord_lon=weather_data['coord_lon']
        )

        return formatted_weather_data

    except Exception:
        raise HttpError(404, 'The desired city or country was not found!')