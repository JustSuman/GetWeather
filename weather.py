import datetime as dt
import requests
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
# my API key
API_KEY = "ff481f559fea02934cdb1cf3a79b991a"
# your city
CITY = input("Enter your city: ").lower().capitalize()

# convert the kelvin to celcius
def kelvin_to_celcius(kelvin):
    celcius = kelvin-273.15
    return celcius

url = BASE_URL + "q=" + CITY + "&APPID=" + API_KEY 

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
# convert kelvin to celcius
temp_celcius = kelvin_to_celcius(temp_kelvin)
# convert kelvin to celcius
# feels like
feels_like = kelvin_to_celcius(response['main']['feels_like'])
# humidity
humid = response['main']['humidity']
# print the weather
print(f"Tempreture: {temp_celcius:.2f}°C")
print(f"Feels like: {feels_like:.2f}°C")
print(f"humidity: {humid}%")