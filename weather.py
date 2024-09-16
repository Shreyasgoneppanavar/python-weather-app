from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Dharwad"):
    request_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data=requests.get(request_url).json()

    return weather_data

if __name__=="__mani__":
    print('\n***Get Current conditions ***\n')

    city=input("\nPlease enter a city name: ")

    # Check for empty strings
    if not bool(city.strip()):
        city="Dharwad"

    weather_data=get_current_weather(city)

    print("/n")
    pprint(weather_data)