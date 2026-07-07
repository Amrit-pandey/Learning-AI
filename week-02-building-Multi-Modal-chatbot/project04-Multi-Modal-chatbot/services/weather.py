import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_current_weather(city: str):
    print("Weather tools called")
    print("API KEY:", API_KEY)

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    result = response.json()
    print(result)
    return result 