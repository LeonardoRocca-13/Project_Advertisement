from geopy.geocoders import Nominatim
import requests


def setup_weather(Country: str, City: str):
    # Use of Geopy library to retrieve the latitude and longitude form the name of a city and a country
    geolocator = Nominatim(user_agent="my_user_agent")
    location = geolocator.geocode(City + ',' + Country)

    # Utilization of the Open-Meteo API to retrieve the weather data of the city
    url = f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&current_weather=true"

    # Send a GET request to the weather API and retrieve the JSON response
    weather_data = requests.get(url).json()

    return weather_data['current_weather']
