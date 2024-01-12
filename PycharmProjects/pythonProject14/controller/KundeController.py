from repository.KundeRepo import KundeRepo
from modelle.Kunde import Kunde
from controller.DataRepoController import ShowData
from repository.BestellungRepo import BestellungRepo


clientManager = KundeRepo('kunde.dat')
orderManager = BestellungRepo('bestellung.dat')
def showClients():
    print("Kunde: ")
    ShowData(2)

def addClient():
    name = input("Kundenname: ")
    adress = input("Kundenadresse: ")

    clients: list = clientManager.load() if clientManager.load() else []
    client = Kunde(1, name, adress)
    clients.append(client)
    clientManager.sort(clients)

def updateClients():
    showClients()
    idList = int(input("Die ID des Clients, den Sie aktualisieren möchten: "))
    clients: list = clientManager.load()

    id = clients[idList].id
    name = input("Geben Sie den neuen Namen ein: ")
    adress = input("Geben Sie die neue Adresse ein: ")
    client = Kunde(id, name, adress)
    clientManager.update(idList, client)


def deleteClient():
    showClients()
    id = int(input("Geben Sie die ID des Clients ein, den Sie löschen möchten: "))
    clientManager.remove(id)
    orderManager.remove(id)