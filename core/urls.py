from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from weather.api import weather_router

api = NinjaAPI(title="Waether Application", description="A REST API For a Weather Application", csrf=True)

api.add_router(prefix="/", router=weather_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
