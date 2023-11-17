from ninja import Schema


class WeatherInSchema(Schema):
    city: str 
    country: str 


class WeatherOutSchema(Schema):
    min_temperature: str
    max_temperature: str
    wind_speed: str
    pressure: str
    humidity: str
    coord_lat: str
    coord_lon: str