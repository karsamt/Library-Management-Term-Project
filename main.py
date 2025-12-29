import catalog, patron, circulation, storage, reports
from datetime import datetime

DATA_DIR = "data"

def librarian_menu(books, patrons, loans):
    while True:
        print("\n--- LIBRARIAN MENU ---")
        print("1) Add Book\n2) Update Book\n3) Search/Filter\n4) Overdues\n5) Fines\n6) Back")
        choice = input("Choice: ")

        if choice == "2":
            isbn = input("Enter ISBN to update: ")
            print("Enter new values (Leave blank to keep current):")
            updates = {
                "title": input("New Title: "),
                "genre": input("New Genre: "),
                "year": input("New Year: "),
                "copies": input("New Total Copies: ")
            }
 
            actual_updates = {k: v for k, v in updates.items() if v}
            res = catalog.update_book(books, isbn, actual_updates)
            print(f"Updated!\n{res}")

        elif choice == "3":
            print("1) Keyword Search\n2) Genre/Year Filter")
            sub = input("> ")
            if sub == "1":
                kw = input("Keyword: ")
                for b in catalog.search_books(books, kw): print(b)
            else:
                g = input("Genre (blank for all): ")
                y = input("Year (blank for all): ")
                res = catalog.filter_books(books, genre=g if g else None, year=y if y else None)
                for b in res: print(b)
        
        elif choice == "5":
            fines = reports.fines_summary(patrons)
            if not fines: print("No outstanding fines.")
            for name, amount in fines.items(): print(f"{name}: {amount} TL")
            
        elif choice == "6": break
        storage.save_state(DATA_DIR, books, patrons, loans)


def patron_menu(books, patrons, loans):
    print("\n1) Login\n2) Register")
    mode = input("Choice: ")
    
    user = None
    if mode == "2":
        data = {
            "library_id": input("ID: "), "name": input("Name: "),
            "email": input("Email: "), "password": input("Password: ")
        }
        patron.register_patron(patrons, data)
        print("Registered! Please login.")
    
    lib_id = input("Library ID: ")
    pwd = input("Password: ")
    user = patron.authenticate_patron(patrons, lib_id, pwd)

    if not user:
        print("Invalid credentials!")
        return

    while True:
        print(f"\n--- WELCOME {user.name} ---")
        print("1) Search Books\n2) Borrow Book\n3) Return Book\n4) My Fines\n5) Logout")
        choice = input("Choice: ")

        if choice == "1":
            kw = input("Keyword: ")
            for b in catalog.search_books(books, kw): print(b)
        elif choice == "2":
            isbn = input("ISBN to borrow: ")
            res = circulation.checkout_book(books, patrons, loans, isbn, user.library_id, 14)
            print(res)
        elif choice == "3":
            loan_id = input("Loan ID to return: ")
            today = datetime.now().strftime("%Y-%m-%d")
            res = circulation.return_book(books, patrons, loans, loan_id, today)
            print(res)
        elif choice == "4":
            print(f"Total Fines: {user.fines} TL")
        elif choice == "5": break
        storage.save_state(DATA_DIR, books, patrons, loans)

def main():
    books, patrons, loans = storage.load_state(DATA_DIR)
    while True:
        print("\n=== YEDITEPE LIBRARY SYSTEM ===")
        print("1) Librarian\n2) Patron\n9) Exit")
        choice = input(">>>> ")
        if choice == "1": librarian_menu(books, patrons, loans)
        elif choice == "2": patron_menu(books, patrons, loans)
        elif choice == "9": break

if __name__ == "__main__":
    main()