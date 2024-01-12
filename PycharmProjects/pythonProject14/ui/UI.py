from controller.MeniuController import showMenu, addDrink, addCookedDish, search, showupdatedmenu, showmenuafterdelete
from controller.KundeController import showClients, addClient, deleteClient, updateClients
from controller.BestellungController import showOrders, searchbyAddress, searchclientName, newOrder, addCLientsOrder


def Console():
    choose = {
    1: menuConsole,
    2: clientConsole,
    3: orderConsole
    }

    while True:
        print("""
        1 - Menu
        2 - Kunden
        3 - Bestellungen
        0 - Exit
        """)
        option = int(input("Wähle eine Option"))
        if option == 0:
            exit()

        choose[option]()


def dishType():
    value = int(input("""
    Wählen Sie die Art des Gerichts aus, das Sie hinzufügen möchten
        1 - Gekochter Gericht
        2 - Getränk
    """))

    options = {
        1: addCookedDish,
        2: addDrink
    }

    options[value]()
    print("Artikel hinzugefügt")
    menuConsole()


def menuConsole():
    while True:
        value = int(input(""" 
        1 - Zeige Menu
        2 - Gericht suchen
        3 - Fügen Sie dem Menu einen neuen Gericht hinzu
        4 - Ein Gericht aktualisieren
        5 - Ein Gericht löschen
        0 - Back
        """))

        options = {
            1: showMenu,
            2: search,
            3: dishType,
            4: showupdatedmenu,
            5: showmenuafterdelete,
            0: Console
        }


        options[value]()

        menuConsole()

def clientConsole():
    while True:
        value = int(input("""
            1 - Alle Kunden anzeigen
            2 - Fügen Sie einen neuen Kunden hinzu
            3 - Löschen Sie einen Kunden
            4 - Aktualisieren Sie einen Client
            0 - Back
        """))

        options = {
            1: showClients,
            2: addClient,
            3: deleteClient,
            4: updateClients,
            0: Console
        }

        options[value]()
        clientConsole()



def orderConsole():
    while True:
        value = int(input(""" 
            1 - Alle Bestellungen anzeigen
            2 - Fügen Sie eine neue Bestellung hinzu
            0 - Back
        """))

        options = {
            1: showOrders,
            2: selectClientConsole,
            0: Console
        }

        options[value]()

def selectClientConsole():
    value = int(input("""  
        1 - Suchen Sie den Kunden nach Namen
        2 - Kunden nach Adresse durchsuchen
        3 - Fügen Sie einen neuen Kunden und eine neue Bestellung hinzu
        0 - Back
    """))


    options = {
        1: searchclientName,
        2: searchbyAddress,
        3: addCLientsOrder,
        0: orderConsole
    }

    options[value]()

    newOrder()