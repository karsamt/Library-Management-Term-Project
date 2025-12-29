CSE101 Term Project - Library Management System 
This project was written in Python to simplify library tasks. The project primarily tracks books, members, and book borrowing/returning events.


How to Run It? If Python is installed on your computer, simply run the main.py file. You will need the data/ folder for the data, but the code has an automatic creation feature; if the folder doesn't exist, it will create it itself.


What Do the Files Do?

main.py: The program's entry point; all menus and screens are here.

catalog.py: Handles adding, deleting, searching, and filtering books.

patron.py: Member registration, login processes, and debt tracking are handled here.

circulation.py: The logic for borrowing books, returning them, and calculating late fees is implemented here.

storage.py: Ensures data is properly saved to JSON files and backed up.

reports.py: Generates reports such as who has overdue books and how much each member owes.


Some Rules and Limits

I limited members to borrowing a maximum of 5 books at a time.

If the book return date passes, the system automatically deducts a daily fine of 2.0 TL.

When searching for books, you can search by both title and author. Additionally, we can filter by year and genre.


Example Flow

First, we log in as the librarian and add books, then we register from the patron (member) menu and borrow that book. The system saves everything to the JSON files in the data/ directory.
