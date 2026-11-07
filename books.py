import json


def show_books(books):
    print("Your Books: ")

    for i, book in enumerate(books, start=1):
        print(f"{i}. {book['name']} - Priority: {book['priority'].upper()}")


def load_books():
    try:
        with open("books.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_books(books):
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)
