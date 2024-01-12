from repository.BestellungRepo import BestellungRepo
from repository.KundeRepo import KundeRepo
from controller.MeniuController import showMenu, drinkManager, cookedDishManager
from controller.KundeController import addClient
from controller.DataRepoController import ShowData
from modelle.Bestellung import Bestellung

orderManager = BestellungRepo('bestellung.dat')
clientManager = KundeRepo('kunde.dat')

def searchclientName():
    name = input("Geben Sie den Namen des gesuchten Clients ein: ")
    clients = clientManager.load() if clientManager.load() else []
    print('\n')
    ids = []
    if clients:
        print("Kunde: ", '\n')
        for idx in range(len(clients)):
            if name.lower() in clients[idx].name.lower():
                print(idx, str(clients[idx]))
                ids.append(clients[idx].id)


def searchbyAddress():
    address = input("Geben Sie die Adresse des gesuchten Kunden ein: ")
    clients = clientManager.load() if clientManager.load() else []
    print('\n')
    ids = []
    if clients:
        print("Kunde: ", '\n')
        for idx in range(len(clients)):
            if address.lower() in clients[idx].address.lower():
                print(idx, str(clients[idx]))


def addCLientsOrder():
    print('\n', "Kunde: ")
    ShowData(2)
    addClient()

def newOrder():
    value = int(input("Geben Sie den ID des Kunden ein, der bestellt: "))
    ShowData(2)
    clients = clientManager.load()
    client = clients[value]

    cookeddishesIds = []
    drinksIds = []
    cookeddishes = cookedDishManager.load() if cookedDishManager.load() else []
    drinks = drinkManager.load() if drinkManager.load() else []

    showMenu()

    while True:
        choose = int(input("""
        Geben Sie ein, was Sie hinzufügen möchten
        1 - ein gekochtes Gericht
        2 - ein Getränk 
        0 - Exit
        """))

        if choose == 0:
            break

        if choose == 1:
            id = int(input("id: "))
            if id < len(cookeddishes):
                cookeddishesIds.append(cookeddishes[id].id)
            else:
                print("Nicht gefunden")
        else:
            id = int(input("id: "))
            if id < len(drinks):
                drinksIds.append(drinks[id].id)
            else:
                print("Nicht gefunden")

    order = Bestellung(1, client.id, cookeddishesIds, drinksIds)
    orders = orderManager.load() if orderManager.load() else []
    orders.append(order)
    orderManager.sort(orders)

    order.printReceipt()



def showOrders():
    print("Bestellungen: ", '\n')
    ShowData(3)

    orders = orderManager.load()
    value = int(input("Zeigen Sie den Beleg der gewünschten Bestellung vor: "))
    orders[value].printReceipt()