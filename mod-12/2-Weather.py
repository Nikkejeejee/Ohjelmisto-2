import requests

api_key = 'YOUR_API_KEY'

def get_weather_info(city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # This will return temperature in Celsius
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature_celsius = data['main']['temp']
        return weather_description, temperature_celsius
    else:
        print("Error fetching data. Make sure you have entered a valid city name.")
        return None

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def main():
    city_name = input("Enter the name of a municipality: ")
    weather_info = get_weather_info(city_name)

    if weather_info:
        description, temperature_kelvin = weather_info
        temperature_celsius = kelvin_to_celsius(temperature_kelvin)
        print(f"Weather in {city_name}: {description}")
        print(f"Temperature: {temperature_celsius:.2f}°C")

if __name__ == "__main":
    main()
