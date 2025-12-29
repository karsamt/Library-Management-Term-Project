from datetime import datetime, timedelta

def checkout_book(books: list, patrons: list, loans: list, isbn: str, library_id: str, period: int) -> dict:
    book = next((b for b in books if b.isbn == isbn), None)
    patron = next((p for p in patrons if p.library_id == library_id), None)

    if not book or not patron: return {"error": "Not found"}
    if book.copies_available <= 0: return {"error": "No copies left"}
    if patron.borrowed_count >= patron.limit: return {"error": "Limit reached"} 

  
    book.copies_available -= 1
    patron.borrowed_count += 1
    due_date = (datetime.now() + timedelta(days=period)).strftime("%Y-%m-%d")
    
    new_loan = {
        "loan_id": str(len(loans) + 1),
        "isbn": isbn,
        "library_id": library_id,
        "due_date": due_date,
        "status": "active"
    }
    loans.append(new_loan)
    return new_loan 

def return_book(books: list, patrons: list, loans: list, loan_id: str, return_date: str) -> dict:
    loan = next((l for l in loans if l['loan_id'] == loan_id and l['status'] == "active"), None)
    if not loan: return {"error": "Loan not found"}

    book = next((b for b in books if b.isbn == loan['isbn']), None)
    patron = next((p for p in patrons if p.library_id == loan['library_id']), None)

    
    due = datetime.strptime(loan['due_date'], "%Y-%m-%d")
    ret = datetime.strptime(return_date, "%Y-%m-%d")
    if ret > due:
        days_late = (ret - due).days
        fine = days_late * 2.0 
        patron.fines += fine
    
    loan['status'] = "returned"
    book.copies_available += 1
    patron.borrowed_count -= 1
    return loan

def overdue_report(loans: list, current_date: str) -> list:
    today = datetime.strptime(current_date, "%Y-%m-%d")
    overdues = []
    for loan in loans:
        if loan['status'] == "active":
            due_date = datetime.strptime(loan['due_date'], "%Y-%m-%d")
            if due_date < today:
                overdues.append(loan)
    return overdues

def fines_summary(patrons: list) -> dict:
    
    summary = {}
    for p in patrons:
        if p.fines > 0:
            summary[p.name] = p.fines
    return summary

def circulation_stats(loans: list, books: list) -> dict:
    stats = {}
    for l in loans:
        isbn = l['isbn']
        stats[isbn] = stats.get(isbn, 0) + 1
    return stats