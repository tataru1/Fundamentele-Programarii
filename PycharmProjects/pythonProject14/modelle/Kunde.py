from modelle.Identifizierbar import Identifizierbar

class Kunde(Identifizierbar):
    def __init__(self, id, name, address):
        super().__init__(id)
        self.name = name
        self.address = address

    def __lt__(self, other):
        return self.name < other.name


    def __str__(self):
        return f"ID={self.id}, Name={self.name}, Adresse={self.address}"