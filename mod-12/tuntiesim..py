import requests

query = input("Anna hakusana:  ")

# Kaksi tapaa hakea dataa request ja respondilla
# Ensimmäinen tapa
request = f"https://api.tvmaze.com/search/shows?q={query}"
response_content = requests.get(request).json()
print(response_content)
# Toinen tapa
# print(requests.get("https://api.tvmaze.com/search/shows?q=girls"))

for show in response_content:
    # suodatetaan hakutulos näyttämään vain isommat watch scoret
    if show["score"] > 0.5:
        print(show["show"]["name"])
        print(show["score"])
        # Tulostetaan genret (jos niitä on)
        for genre in show["show"]["genres"]:
            print(f" - {genre}")
