from geopy.geocoders import Nominatim
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain import LLMChain
import random as rd
import requests
import pprint
import os


def setup_api_openai(API_key: str):
    # Get the API key of the user
    os.environ["OPENAI_API_KEY"] = API_key

    # Define the language model and the temperature
    llm = OpenAI(
        model_name="text-davinci-002",
        temperature=1
    )

    return llm


"""

esempio del json di risposta
current_weather": {
    "time": "2022-07-01T09:00",
    "temperature": 13.3,
    "weathercode": 3,
    "windspeed": 10.3,
    "winddirection": 262
}
    
"""


def setup_weather(Country: str, City: str):
    geolocator = Nominatim(user_agent="my_user_agent")
    localisation = geolocator.geocode(City + ',' + Country)

    url = f"https://api.open-meteo.com/v1/forecast?latitude={localisation.latitude}&longitude={localisation.longitude}&current_weather=true"
    weather_data = requests.get(url).json()

    return weather_data

if __name__ == "__main__":
    pprint.pprint(setup_weather("Italy", "Rome"))
