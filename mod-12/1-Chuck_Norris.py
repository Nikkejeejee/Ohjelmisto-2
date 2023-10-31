import requests


def get_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"

    try:
        response = requests.get(url)
        response.raise_for_status()
        joke_data = response.json()
        joke_text = joke_data["value"]
        return joke_text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def main():
    joke = get_random_chuck_norris_joke()
    if joke:
        print("Chuck Norris Joke:")
        print(joke)


if __name__ == "__main__":
    main()
