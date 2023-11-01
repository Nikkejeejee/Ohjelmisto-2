import requests

url = "https://api.chucknorris.io/jokes/random/"

try:
    res = requests.get(url).json()
    joke = res['value']
    print(joke)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except ValueError as e:
    print(f"Error parsing the JSON response: {e}")
