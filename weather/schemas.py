from ninja import Schema, Field


class WeatherInSchema(Schema):
    city: str = Field(..., max_length=20)
    country: str = Field(..., max_length=20)


class WeatherOutSchema(Schema):
    min_temperature: str
    max_temperature: str
    wind_speed: str
    pressure: str
    humidity: str
    coord_lat: str
    coord_lon: str