from geopy.geocoders import Nominatim

from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain import LLMChain

import requests
import os

from libraries.utils.get_path import get_path
from libraries.utils.settings import OPENAI_API_KEY_FILE_NAME, RESOURCES_FOLDER_NAME, WEATHER_INDEX_FILE_NAME


def setup_api_openai():
    # Get the API key for OpenAI from the file 'openai_api_key.txt' in the resources folder
    main_dir_path = get_path()
    file_path = os.path.join(main_dir_path, RESOURCES_FOLDER_NAME, OPENAI_API_KEY_FILE_NAME)
    try:
        with open(file_path, 'r') as key_file:
            api_key = key_file.readline()
    except FileNotFoundError:
        print("Please enter your OpenAI API key in the file 'openai_api_key.txt' in the root folder of the project.")
        exit(1)

    os.environ["OPENAI_API_KEY"] = api_key

    # Define the large language model and the relative temperature
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=1
    )

    return llm


def setup_weather(Country: str, City: str):
    # Use of Geopy library to retrieve the latitude and longitude form the name of a city and a country
    geolocator = Nominatim(user_agent="my_user_agent")
    location = geolocator.geocode(City + ',' + Country)

    # Utilization of the Open-Meteo API to retrieve the weather data of the city
    url = f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&current_weather=true"

    # Send a GET request to the weather API and retrieve the JSON response
    weather_data = requests.get(url).json()

    return weather_data['current_weather']


def generate_prompt(weather: dict, llm, bio_info: tuple, flight_info: tuple, product: str):
    # Unpack the lists containing the information about the person and the flight
    age, gender, emotion = bio_info
    flight_duration, time_before_departure, airline_company = flight_info

    # Get the json file containing the weather index from the resources folder
    main_dir_path = get_path()
    file_path = os.path.join(main_dir_path, RESOURCES_FOLDER_NAME, WEATHER_INDEX_FILE_NAME)
    with open(main_dir_path, 'r') as json_file:
        json_context = json_file.read()

    # Define the prompt template with placeholders for variables
    template = """
    Write a targeted 1 short sentence long advertisement knowing the following information about the person:
    {gender}, {age} years old, who is currently feeling {emotion}.
    You should keep in mind that our target is a person taking a {flight_duration} flight, has {time_before_departure}
    left before departure, and flies with {airline_company} so keep it in mind to target the pricing accordingly.
    Capture their attention and emphasize how this {product} knowing that the meteo in the city the person is currently in is {weather}.
    Use this json file to decode the weather context but don't show anything in the ad: {json_context}.
    The output should exclude any personal information about the person and should adress the target personally,
    (speaking to him like a friend), and the him why he should be interested to the ad.
    """

    # Create a prompt template with defined variables
    prompt = PromptTemplate(
        template=template,
        input_variables=['sex', 'age', 'mood', 'flight_duration', 'time_before_departure', 'airline_company',
                         'products', 'context', 'json_context'],
    )

    # Create an LLMChain instance with the prompt and language model
    llm_chain = LLMChain(
        prompt=prompt,
        llm=llm,
        verbose=True
    )

    # Run the language model chain with the provided variables and return the results
    results = llm_chain.run(
        sex=sex,
        age=age,
        mood=mood,
        flight_duration=flight_duration,
        time_before_departure=time_before_departure,
        airline_company=airline_company,
        products=products,
        context=context,
        json_context=json_context
    )

    return results
