import json
class Book:
    
    def __init__(self, isbn, title, authors, year, genre, copies, copies_available):
        self.isbn=isbn
        self.title=title
        self.authors=authors
        self.year=year
        self.genre=genre
        self.copies=copies
        self.copies_available=copies_available

    def to_dict(self):
        return {"isbn":self.isbn,
                "title":self.title,
                "authors":self.authors,
                "year":self.year,
                "genre":self.genre,
                "copies":self.copies,
                "copies_available":self.copies_available
        }
    
    def __repr__(self):
        return f"Title:{self.title} | Authors: {', '.join(self.authors)}"
    
def save_books(path, book_list):
    dict_list=[book.to_dict() for book in book_list]
    with open(path, "w", encoding="utf-8") as file:
        json.dump(dict_list, file, indent=4)

def load_books(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            dict_list=json.load(file)
    except FileNotFoundError:
        dict_list=[]
    
    book_list=[]
    for book_dict in dict_list:
        book=Book(**book_dict)
        book_list.append(book)
    
    return book_list

def add_book(book_list:list, book_data:dict):
    new_book=Book(**book_data)
    book_list.append(new_book)
    
    return new_book.to_dict()

def search_books(book_list, keyword):
    search_results=[]
    keyword=keyword.lower()
    
    for book in book_list:
        if keyword in book.title.lower():
            search_results.append(book)
            continue
        for author in book.authors:
            if keyword in author.lower():
                search_results.append(book)
                break
    
    return search_results

def filter_books(book_list, genre:str=None, year:int=None):
    filtered_book_list=[]
    
    for book in book_list:
        genre_matches=False
        year_matches=False
        
        if genre is None:
            genre_matches=True    
        elif genre.lower() in book.genre.lower():
            genre_matches=True
                                                             #checks both genre and year filters if there is any given.
        if year is None:
            year_matches=True    
        elif year==book.year:
            year_matches=True
        
        if year_matches and genre_matches:
            filtered_book_list.append(book)
    
    return filtered_book_list

def update_book(book_list:list, isbn:str, update_data:dict):
    book_to_be_updated=None
    for book in book_list:
        if isbn==book.isbn:
            book_to_be_updated=book
            break
    if book_to_be_updated:
        for attribute, value in update_data.items():
            if hasattr(book_to_be_updated, attribute):
                setattr(book_to_be_updated, attribute, value)
        return book_to_be_updated.to_dict()
           
            
