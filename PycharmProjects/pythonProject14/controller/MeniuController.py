from repository.GetränkRepo import GetränkRepo
from repository.GekochterGerichtRepo import GekochterGerichtRepo
from modelle.GekochterGericht import GekochterGericht
from modelle.Getränk import Getränk
from controller.DataRepoController import ShowData

cookedDishManager = GekochterGerichtRepo('gekochtergericht.dat')
drinkManager = GetränkRepo('getrank.dat')

def showMenu():
    print("Gekochte Gerichte: ")
    ShowData(0)

    print("Getränke: ")
    ShowData(1)

def addCookedDish():
    name = input("Name des gekochten Gerichts: ")
    portionSize = int(input("Portionsgröße des gekochten Gerichts: "))
    price = int(input("Preis des zubereiteten Gerichts: "))
    prepTime = int(input("Zubereitungszeit des gekochten Gerichts:"))

    cookedDishes = cookedDishManager.load() if cookedDishManager.load() else []
    cookedDish = GekochterGericht(name, portionSize, price, prepTime)
    cookedDishes.append(cookedDish)
    cookedDishManager.sort(cookedDishes)


def addDrink():
    name = input("Name des Getränks: ")
    portionSize = int(input("Portionsgröße des Getränks: "))
    price = int(input("Preis des Getränks: "))
    alcoolVolume = int(input("Alkoholgehalt des Getränks: "))

    drinks = drinkManager.load() if drinkManager.load() else []
    drink = Getränk(name, portionSize, price, alcoolVolume)
    drinks.append(drink)
    drinkManager.sort(drinks)

def search():
    name = input("Geben Sie den Namen des gesuchten Artikels ein: ")
    cookeddishes = cookedDishManager.load() if cookedDishManager else []
    drinks = drinkManager.load() if drinkManager else []
    print('\n')
    if cookeddishes:
        print("Gekochte Gerichte: ", '\n')
        for idx in range(len(cookeddishes)):
            if name.lower() in cookeddishes[idx].id.lower():
                print(idx, str(cookeddishes[idx]))

    if drinks:
        print("Getränke: ", '\n')
        for idx in range(len(drinks)):
            if name.lower() in drinks[idx].id.lower():
                print(idx, str(drinks[idx]))

        return

    print("kein solcher Artikel gefunden")

def updateItem():
    choose = int(input("""
    Geben Sie die Art des Gerichts ein, das Sie aktualisieren möchten:
        1 - Gekochter Gericht
        2 - Getränk
    """))
    id = int(input("Geben Sie die ID des Gerichts ein, das Sie aktualisieren möchten"))
    if choose == 1:
        name = input("Geben Sie den neuen Namen des zubereiteten Gerichts ein: ")
        portionSize = input("Geben Sie die neue Portionsgröße ein: ")
        price = input("Geben Sie den neuen Preis ein: ")
        prepTime = input("Geben Sie die neue Zubereitungszeit ein: ")
        cookedDish = GekochterGericht(name,  portionSize, price, prepTime)
        cookedDishManager.update(id, cookedDish)

    else:
        name = input(("Geben Sie den neuen Namen des Getränks ein: "))
        portionsize = input("Geben Sie die neue Portionsgröße ein: ")
        price = input("Geben Sie den neuen Preis ein: ")
        alcoholvolume = input("Geben Sie den neuen Alkoholgehalt ein: ")
        drink = Getränk(name, portionsize, price, alcoholvolume)
        drinkManager.update(id, drink)

def showupdatedmenu():
    showMenu()
    updateItem()

def deleteItem():
    choose = int(input("""
    Geben Sie ein, was Sie löschen möchten:
        1 - Gekochter Gericht
        2 - Getränk
    """))

    id = int(input("Geben Sie die ID des Gerichts ein, das Sie löschen möchten: "))
    if choose == 1:
        cookedDishManager.remove(id)
    else:
        drinkManager.remove(id)

def showmenuafterdelete():
    showMenu()
    deleteItem()