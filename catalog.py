import json

class Book:
    def __init__(self, isbn, title, authors, year, genre, copies, copies_available, active=True):
        self.isbn = isbn
        self.title = title
        self.authors = authors
        self.year = int(year)
        self.genre = genre
        self.copies = int(copies)
        self.copies_available = int(copies_available)
        self.active = active 

    def to_dict(self):
        return self.__dict__

    def __repr__(self):
        return f"Title: {self.title} | Available: {self.copies_available}/{self.copies}"

def load_books(path: str) -> list:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return [Book(**b) for b in json.load(file)]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(path: str, books: list) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump([b.to_dict() for b in books], file, indent=4)

def add_book(books: list, book_data: dict) -> dict:
    new_book = Book(**book_data)
    books.append(new_book)
    return new_book.to_dict()

def search_books(books: list, keyword: str) -> list:

    kw = keyword.lower()

    return [b for b in books if b.active and (kw in b.title.lower() or any(kw in a.lower() for a in b.authors))]



def filter_books(books: list, genre: str = None, year: int = None) -> list:


    results = [b for b in books if b.active]

    if genre:

        results = [b for b in results if b.genre.lower() == genre.lower()]

    if year:

        results = [b for b in results if b.year == int(year)]

    return results

def update_book(books: list, isbn: str, updates: dict) -> dict:
    for b in books:
        if b.isbn == isbn:
            for key, val in updates.items():
                if hasattr(b, key):
                    setattr(b, key, val)
            try:
                b.year=int(b.year)
                b.copies=int(b.copies)
                b.copies_available=b.copies
            except ValueError:
                print("Year and/or Copy amount should be integers.")
                print("Updating is interrupted.")
                return None
                
            return b.to_dict()
    return None