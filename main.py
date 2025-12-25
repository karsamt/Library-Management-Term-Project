import catalog

def interface(): 
    while True:
        selection=input("                                   LIBRARY MANAGEMENT SYSTEM\n                    1)Select 1 if you are a Librarian\n                    2)Select 2 if you are a Patron\n                    3)Select 9 if you want to quit")
        if selection=="9":
            confirming=input("Confirm quitting by selecting 9 again.")
            if confirming=="9":
                print("EXİTİNG")
                break
        elif selection=="1":
            pass
        elif selection=="2":
            pass

if __name__=="__main__":                   #checks if main.py is the main executed file, i dont know if its necessary for my project but i saw that it is important for preventing import issues
    book_list=catalog.load_books("data/books.json")
    interface()