import json
import os

DEFAULT_WORDS = {"sun": "aurinko", "moon": "kuu", "star": "tähti"}
DATA_FILE = "translations.json"

def load_words():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (OSError, json.JSONDecodeError) as error:
            print(f"Error loading file: {error}\nUsing default words.")
    return DEFAULT_WORDS.copy()

def save_words(word_list):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(word_list, file, ensure_ascii=False, indent=4)
        print("Translations saved!")
    except OSError as error:
        print(f"Error saving translations: {error}")

def word_translator():
    word_list = load_words()

    while True:
        word = input("\nEnter a word (press Enter to exit): ").strip().lower()

        if not word:
            save_words(word_list)
            print("Session closed. Changes saved.")
            break

        if word in word_list:
            print(f"{word} translates to '{word_list[word]}'")
        else:
            print("Word not found.")
            meaning = input("Enter its translation (or press Enter to skip): ").strip().lower()
            if meaning:
                word_list[word] = meaning
                print(f"Added: {word} = {meaning}")

if __name__ == "__main__":
    word_translator()
