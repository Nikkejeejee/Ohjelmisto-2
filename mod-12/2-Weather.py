import requests

def kelvin_to_celsius(kelvin_temp):
    celsius_temp = kelvin_temp - 273.15
    return round(celsius_temp, 2)

def get_weather_data(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature_kelvin = data['main']['temp']
            temperature_celsius = kelvin_to_celsius(temperature_kelvin)
            return f"Sää {city}: {weather_description}, lämpötila: {temperature_celsius} °C"
        else:
            return "Tietoja ei löytynyt."

    except requests.exceptions.RequestException as e:
        return f"Virhe: {e}"

if __name__ == '__main__':
    api_key = "TÄHÄN_API-AVAIN"  # Korvaa tämä oma API-avaimellasi
    city = input("Anna paikkakunnan nimi: ")
    weather_data = get_weather_data(api_key, city)
    print(weather_data)
