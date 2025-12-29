import catalog

def interface(book_lst): 
    while True:
        selection=input("\n\n\n                                   LIBRARY MANAGEMENT SYSTEM\n\n\n\n                    1)Select 1 if you are a Librarian\n                    2)Select 2 if you are a Patron\n                    3)Select 9 if you want to quit\n>>>>>>")
        
        if selection=="9":
            confirming=input("Confirm quitting by selecting 9 again.")
            if confirming=="9":
                print("EXİTİNG")
                break
        
        elif selection=="1":
            while True:
                print("                                   LIBRARIAN MENU")
                print("                    1)Add New Book")
                print("                    2)Update Book")
                print("                    3)Search/Filter Books")
                print("                    4)Go To The Main Menu")
                librarian_selection=input("Select the number of the action you want to take:")
                
                if librarian_selection=="1":
                    new_isbn=input("ISBN(format:000-0000000000):")
                    new_title=input("Title:")
                    new_authors_str=input("Author, seperated with (-) if multiple:")
                    new_year=input("Publication year:")
                    new_genre=input("Genre of the book:")
                    while True:
                        new_copies=input("Copy amount:")
                        try:
                            new_copies=int(new_copies)
                            break
                        except ValueError:
                            print(" copy amount must be integer")
                    print("Adding the Book...")
                    new_authors=new_authors_str.split("-")
                    new_book_data={
                        "isbn":new_isbn,
                        "title":new_title,
                        "authors":new_authors,
                        "year":new_year,
                        "genre":new_genre,
                        "copies":new_copies,
                        "copies_available":new_copies
                    }
                    print(f"                    ADDED {new_title}:\n{catalog.add_book(book_lst,new_book_data)}")
                
                elif librarian_selection=="2":
                    isbn_to_be_updated=input("Enter The ISBN of the book that is going to be updated:")
                    for book in book_lst:
                        if book.isbn==isbn_to_be_updated:
                            book_to_be_updated=book
                            break
                    print(f"Current Data of {book_to_be_updated.title}:\n{book_to_be_updated.to_dict()}")
                    updated_isbn=input("ISBN(format:000-0000000000):")
                    updated_title=input("Title:")
                    updated_authors_str=input("Author, seperated with (-) if multiple:")
                    updated_year=input("Copy count:")
                    updated_genre=input("Genre of the book:")
                    while True:
                        updated_copies=input("Publication year:")
                        try:
                            updated_copies=int(updated_copies)
                            break
                        except ValueError:
                            print("Copy amount should be integer")
                    print("Updating the Book...")
                    updated_authors=updated_authors_str.split("-")
                    new_book_data={
                        "isbn":updated_isbn,
                        "title":updated_title,
                        "authors":updated_authors,
                        "year":updated_year,
                        "genre":updated_genre,
                        "copies":updated_copies,
                    }
                    
                    print(f"                    UPDATED DATA OF THE {book_to_be_updated.title}:\n{catalog.update_book(book_lst, isbn_to_be_updated, new_book_data)}")

                
                elif librarian_selection=="3":
                    pass
                
                elif librarian_selection=="4":
                    print("\n\n\n\n\n\n\n\n\n\n\n\n")
                    break                
        
        elif selection=="2":
            pass
        
        
        else :
            print("                                   !!!İNVALİD SELECTİON!!!")

if __name__=="__main__":                   #checks if main.py is the main executed file, i dont know if its necessary for my project but i saw that it is important for preventing import issues
    book_list=catalog.load_books("data/books.json")
    interface(book_list)