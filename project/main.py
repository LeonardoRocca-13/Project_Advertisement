import random

from libraries.utils.api_openai import get_openai_model
from libraries.text_generation import generate_prompt
from libraries.vison_detection import capture_frame
from libraries.utils.weather import get_weather
from libraries.windows import UserAgreementWindow


def greeting_window():
    UserAgreementWindow().run()


def webcam_window():
    bio_info = capture_frame()
    return bio_info


def flight_window():
    location = get_random_location()
    weather = get_weather(location)
    flight_info = get_flight_info()

    return flight_info, weather


def ad_window(ad_text: str):
    # kuz stuffs!
    print(ad_text)


def get_flight_info():
    sample_flight_durations = ["1:30 hours", "45 minutes", "7:45 hours", "3 hours"]
    sample_time_before_departures = ["30 minutes", "15 minutes", "1:45 hours", "1:03 hours"]
    sample_airline_companies = ["Ryanair", "Alitalia", "Lufthansa", "Air France"]

    flight_duration = random.choice(sample_flight_durations)
    time_before_departure = random.choice(sample_time_before_departures)
    airline_company = random.choice(sample_airline_companies)

    return flight_duration, time_before_departure, airline_company


def get_random_location():
    cities = ["Rome", "Paris", "London", "Casablanca", "New York", "Tokyo", "Canberra", "Lima", "Singapore"]
    countries = ["Italy", "France", "United Kingdom", "Morocco", "United States", "Japan", "Australia", "Peru", "Singapore"]

    locations = tuple(zip(cities, countries))
    return random.choice(locations)


def get_random_product():
    products = {
        "Coffee": ["Starbucks", "Lavazza", "Nespresso"],
        "Sport Shoes": ["Nike", "Adidas", "Puma"],
        "Headphones": ["Sony", "Bose", "JBL"],
        "Sunglasses": ["Ray-Ban", "Oakley", "Persol"],
        "Smartphone": ["Apple", "Samsung", "Huawei"],
        "Laptop": ["Apple", "Dell", "HP"],
        "Car": ["Fiat", "Ford", "BMW"]
    }

    product = random.choice(list(products.keys()))
    brand = random.choice(products[product])

    return f"{brand}, {product}"


def get_ad(bio_info: tuple, weather: str, flight_info: tuple, product: str):
    llm = get_openai_model()
    ad_text = generate_prompt(weather, llm, bio_info, flight_info, product)

    return ad_text


def main():
    greeting_window()
    bio_info = webcam_window()
    flight_info, weather = flight_window()
    product = get_random_product()
    ad_text = get_ad(bio_info, weather, flight_info, product)
    ad_window(ad_text)


if __name__ == "__main__":
    main()
