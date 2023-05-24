import random

import libraries.vison_detection as vdl
from libraries.windows import UserAgreementWindow
import libraries.text_generation


def greeting_window():
    greeting_window = UserAgreementWindow()
    greeting_window.run()


def webcam_window():
    bio_info = vdl.capture_frame()
    return bio_info


def flight_window():
    #tkinter window
    place = get_place()
    flight_info = get_flight_details()

    return flight_info


def ad_window(info: tuple, flight_info: tuple):
    #tkinter window
    product = get_product()
    ad_text = get_ad(info, flight_info, product)
    print(ad_text)


def get_flight_details():
    sample_flight_durations = ["1:30 hours", "45 minutes", "7:45 hours", "3 hours"]
    sample_time_before_departures = ["30 minutes", "15 minutes", "1:45 hours", "1:03 hours"]
    sample_airline_companies = ["Ryanair", "Alitalia", "Lufthansa", "Air France"]
    flight_duration = random.choice(sample_flight_durations)
    time_before_departure = random.choice(sample_time_before_departures)
    airline_company = random.choice(sample_airline_companies)
    
    flight_infos = (flight_duration, time_before_departure, airline_company)
    
    return flight_infos


def get_place():
    places = ["Rome", "Paris", "London", "Casablanca", "New York", "Tokyo", "Canberra", "Lima", "Singapore"]
    place = random.choice(places)
    match place:
        case "Rome":
            country = "Italy"
        case "Paris":
            country = "France"
        case "London":
            country = "United Kingdom"
        case "Casablanca":
            country = "Morocco"
        case "New York":
            country = "United States"
        case "Tokyo":
            country = "Japan"
        case "Canberra":
            country = "Australia"
        case "Lima":
            country = "Peru"
        case "Singapore":
            country = "Singapore"
            
    return (place, country)


def get_product():
    products = ["Coffee", "Sport Shoes", "Headphones", "Sunglasses", "Smartphone", "Laptop", "Car"]
    product = random.choice(products)
    match product:
        case "Coffee":
            return random.choice(["Starbucks", "Lavazza", "Nespresso"]) + " coffee"
        case "Sport Shoes":
            return random.choice(["Nike", "Adidas", "Puma"]) + " shoes"
        case "Headphones":
            return random.choice(["Sony", "Bose", "JBL"]) + " headphones"
        case "Sunglasses":
            return random.choice(["Ray-Ban", "Oakley", "Persol"]) + " sunglasses"
        case "Smartphone":
            return random.choice(["Apple", "Samsung", "Huawei"]) + " phone"
        case "Laptop":
            return random.choice(["Apple", "Dell", "HP"]) + " computer"
        case "Car":
            return random.choice(["Fiat", "Ford", "BMW"]) + " car"
            
    return product


def get_ad(info: tuple, flight_info: tuple, product: str):
    #calling the function to get the ad text
    ...


def main():
    greeting_window()
    bio_info = webcam_window()
    flight_info = flight_window()
    ad_window(bio_info, flight_info)


if __name__ == "__main__":
    main()
