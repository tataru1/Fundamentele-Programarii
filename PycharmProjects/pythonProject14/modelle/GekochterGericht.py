from modelle.Gericht import Gericht

class GekochterGericht(Gericht):
    def __init__(self, id, portionSize, price, prepTime):
        super().__init__(id, portionSize, price)
        self.prepTime = prepTime

    def __lt__(self, other):
        return self.id < other.id

    def __iter__(self):
        return iter(self.id, self.price)


    def __str__(self):
        return f"ID={self.id}, Portionsgröße={self.portionSize}, Preis={self.price}, Vorbereitungszeit={self.prepTime}"