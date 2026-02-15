import requests
import json
import random
import os

API_URL = "https://official-joke-api.appspot.com/random_joke"
FILE_NAME = "saved_jokes.json"


def load_saved_jokes():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []


def save_joke(joke):
    jokes = load_saved_jokes()
    jokes.append(joke)

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(jokes, file, indent=4)


def get_joke_from_api():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()

        joke = f"{data['setup']} — {data['punchline']}"
        return joke
    except:
        return None


def get_random_saved_joke():
    jokes = load_saved_jokes()
    if jokes:
        return random.choice(jokes)
    return None


def main():
    print("=== Random Joke CLI ===\n")

    joke = get_joke_from_api()

    if joke:
        print("✅ Fetched from API:\n")
        print(joke)
        save_joke(joke)
    else:
        print("⚠ Could not reach API endpoint.\n")

        saved_joke = get_random_saved_joke()
        if saved_joke:
            print("📁 Showing saved joke instead:\n")
            print(saved_joke)
        else:
            print("No saved jokes available. Please connect to the internet first.")


if __name__ == "__main__":
    main()
