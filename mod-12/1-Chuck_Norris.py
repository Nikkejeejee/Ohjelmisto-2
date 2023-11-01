import requests

url = "https://api.chucknorris.io/jokes/random/"

res = requests.get(url).json()
print(res['value'])
