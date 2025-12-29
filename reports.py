from datetime import datetime

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