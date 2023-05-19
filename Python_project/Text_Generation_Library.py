import os

import requests
from geopy.geocoders import Nominatim
from langchain import LLMChain
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI


def setup_api_openai(API_key: str):
    # Get the API key of the user
    os.environ["OPENAI_API_KEY"] = API_key

    # Define the language model and the temperature
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=1
    )

    return llm


def setup_weather(Country: str, City: str):
    geolocator = Nominatim(user_agent="my_user_agent")
    location = geolocator.geocode(City + ',' + Country)

    url = f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&current_weather=true"
    weather_data = requests.get(url).json()

    return weather_data['current_weather']


def generate_prompt(context, llm, infos: tuple):
    sex, age, mood, flight_duration, time_before_departure, airline_company, products = infos

    # Define the prompt template
    template = """
    Write a targeted 1 short sentence long advertisement knowing the following information about the person:
    {sex}, {age} years old, who is currently feeling {mood}.
    You should keep in mind that our target is a person taking a {flight_duration}-hours flight, has {time_before_departure} 
    hours left before departure, and flies with {airline_company} so keep it in mind to target the pricing accordingly. 
    Capture their attention and emphasize how this {products} knowing that the meteo in the city the person is currently in is {context}.
    The output should exclude any personal information about the person and should adress the target personally,
    (speaking to him like a friend), and the him why he should be interested to the ad.
    """

    prompt = PromptTemplate(
        template=template,
        input_variables=['sex', 'age', 'mood', 'flight_duration', 'time_before_departure', 'airline_company',
                         'products', 'context'],
    )

    llm_chain = LLMChain(
        prompt=prompt,
        llm=llm,
        verbose=True
    )

    results = llm_chain.run(
        sex=sex,
        age=age,
        mood=mood,
        flight_duration=flight_duration,
        time_before_departure=time_before_departure,
        airline_company=airline_company,
        products=products,
        context=context
    )

    return results


if __name__ == "__main__":
    llm = setup_api_openai('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')
    weather_data = setup_weather('Rome', 'Italy')
    ad = generate_prompt(weather_data, llm, ['Male', '30', 'Happy', '2', '2', 'Emirates', 'coffee'])

    print(ad)
