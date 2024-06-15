import requests
import json
import sys
from geopy.geocoders import Nominatim

def get_weather(latitude,longitude):

    api_key = "xxxxxxx"
    url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(latitude,longitude,api_key)
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data
    else:
        return None

def main():

    if len(sys.argv) < 2:
        print("Please provide the city name as a command line argument.")
    else:
        city = " ".join(sys.argv[1:])
    latitude, longitude = get_coordinates(city)
    data = get_weather(latitude,longitude)
    if data is not None:
        print("Current weather for {}:".format(city))
        print("Temperature: {}K".format(data["main"]["temp"]))
        print("Humidity: {}%".format(data["main"]["humidity"]))
        print("Pressure: {} hPa".format(data["main"]["pressure"]))
        print("Weather: {}".format(data["weather"][0]["description"]))
    else:
        print("Could not find weather data for {}.".format(city))


def get_coordinates(city):
    geolocator = Nominatim(user_agent="my_app")  
    location = geolocator.geocode(city)
    latitude = location.latitude
    longitude = location.longitude
    return latitude, longitude


if __name__ == "__main__":
    main()
