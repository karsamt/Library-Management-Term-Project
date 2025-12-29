import json

class Patron:
    def __init__(self, library_id, name, email, password, contact_info="", borrowed_count=0, fines=0.0):
        self.library_id = library_id
        self.name = name
        self.email = email
        self.password = password 
        self.contact_info = contact_info
        self.borrowed_count = borrowed_count
        self.fines = fines
        self.limit = 5 

    def to_dict(self):
        return self.__dict__

def load_patrons(path: str) -> list:
    try:
        with open(path, "r") as f:
            return [Patron(**p) for p in json.load(f)]
    except: return []

def save_patrons(path: str, patrons: list) -> None:
    with open(path, "w") as f:
        json.dump([p.to_dict() for p in patrons], f, indent=4)

def register_patron(patrons: list, patron_data: dict) -> dict:
    
    if any(p.library_id == patron_data['library_id'] for p in patrons):
        return {"error": "Duplicate ID"}
    new_p = Patron(**patron_data)
    patrons.append(new_p)
    return new_p.to_dict()

def authenticate_patron(patrons: list, library_id: str, password: str):
    for p in patrons:
        if p.library_id == library_id and p.password == password:
            return p
    return None 