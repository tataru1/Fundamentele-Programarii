from modelle.Identifizierbar import Identifizierbar
from functools import reduce
from controller.MeniuController import drinkManager, cookedDishManager

class Bestellung(Identifizierbar):
    total = 0
    def __init__(self, id, clientId, dishIds, drinkIds):
        super().__init__(id)
        self.clientId = clientId
        self.dishIds = dishIds
        self.drinkIds = drinkIds

    def calculateCost(self):
        cookeddishList = cookedDishManager.load()
        drinkList = drinkManager.load()
        prices = []

        for dish in cookeddishList:
            if dish.id in self.dishIds:
                prices.append(int(dish.price))

        for drink in drinkList:
            if drink.id in self.drinkIds:
                prices.append(int(drink.price))


        self.total = reduce(lambda x, y: x + y, prices)


    def __generateReceipt(self):#private methode
        self.calculateCost()
        cookeddishList = cookedDishManager.load()
        drinkList = drinkManager.load()
        receipt = f"Bestellung: {self.id} für den Client mit der ID {self.clientId}" + '\n'

        ids = []
        prices = []

        for dish in cookeddishList:
            if dish.id in self.dishIds:
                ids.append(dish.id)
                prices.append(str(dish.price))

        for drink in drinkList:
            if drink.id in self.drinkIds:
                ids.append(drink.id)
                prices.append(str(drink.price))

        items = list(map(lambda x, y: f"Artikel: {x}  Preis: {y}" + '\n', ids, prices))

        receipt += "".join(items)
        receipt += f"Total: {str(self.total)}"

        return receipt

    def printReceipt(self):
        receipt = self.__generateReceipt()
        print(receipt)

    def __lt__(self, other):
        return self.id < other.id

    def __str__(self):
        return f"Bestellung: {self.id} Kunde: {self.clientId} GekochteGerichte: {self.dishIds} Getränke: {self.drinkIds}"