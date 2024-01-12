from modelle.Identifizierbar import Identifizierbar

class Gericht(Identifizierbar):
    def __init__(self, id, portionSize, price):
        super().__init__(id)
        self.portionSize = portionSize
        self.price = price