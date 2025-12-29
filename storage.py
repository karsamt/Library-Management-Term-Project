import json
import os
import shutil
from datetime import datetime

def ensure_data_paths(base_dir: str) -> None:
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

def load_state(base_dir: str) -> tuple:

    import catalog, patron, circulation
    books = catalog.load_books(os.path.join(base_dir, "books.json"))
    patrons = patron.load_patrons(os.path.join(base_dir, "patrons.json"))
 
    try:
        with open(os.path.join(base_dir, "loans.json"), "r") as f:
            loans = json.load(f)
    except FileNotFoundError:
        loans = []
    return books, patrons, loans

def save_state(base_dir: str, books: list, patrons: list, loans: list) -> None:

    import catalog, patron
    catalog.save_books(os.path.join(base_dir, "books.json"), books)
    patron.save_patrons(os.path.join(base_dir, "patrons.json"), patrons)
    with open(os.path.join(base_dir, "loans.json"), "w") as f:
        json.dump(loans, f, indent=4)

def backup_state(base_dir: str, backup_dir: str) -> list:

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    files = ["books.json", "patrons.json", "loans.json"]
    backed_up_files = []
    for f in files:
        src = os.path.join(base_dir, f)
        if os.path.exists(src):
            dst = os.path.join(backup_dir, f"{timestamp}_{f}")
            shutil.copy2(src, dst)
            backed_up_files.append(dst)
    return backed_up_files