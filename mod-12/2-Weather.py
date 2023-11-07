import requests


def kelvin_to_celcius(kelvin):
    return kelvin - 273.15


user_input = str(input("Anna paikkakunnan nimi:  "))
api_key = "9f6ee7702beb29c882ac24b1a06f016f"

base_url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'q': user_input,
    'appid': api_key
}

res = requests.get(base_url, params=params)
weather = res.json()

weather_status = weather['weather'][0]['description']
weather_temp = weather['main']['temp']

print(f'''
Kaupunki {user_input}
Säätila: {weather_status}
Lämpötila: {kelvin_to_celcius(weather_temp):.1f} celcius
''')
