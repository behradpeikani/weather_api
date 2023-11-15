from ninja import Schema
    

class WeatherSchema(Schema):
    city: str = Field(..., max_length=20)
    country: str = Field(..., max_length=2)
