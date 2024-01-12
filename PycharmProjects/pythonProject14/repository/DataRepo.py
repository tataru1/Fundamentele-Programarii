import pickle
from abc import abstractmethod

class DataRepo:
    def __init__(self, filename):
        self.filename = filename

    def save(self, objectList):
        with open(self.filename, 'wb') as file:
            pickle.dump(objectList, file)

    def load(self):
        with open(self.filename, 'rb') as file:
            try:
                return pickle.load(file)
            except EOFError:
                print("DATABASE EMPTY")

    def sort(self, objectList):
        objectList = sorted(objectList)
        self.save(objectList)

    def add(self, object):
        objectList: list = self.load()
        objectList.append(object)
        self.sort(objectList)
        print("Neues Element hinzugefügt")

    def remove(self, id):
        objectList: list = self.load()
        if id < len(objectList):
            objectList.pop(id)
            self.save(objectList)
            print("Artikel entfernt")
            return

        print("Artikel nicht gefunden")

    def update(self, id, newObj):
        objectList: list = self.load()
        if id < len(objectList):
            self.remove(id)
            self.add(newObj)
            print("Artikel aktualisiert")
            return

        print("Artikel nicht gefunden")

    @abstractmethod
    def convert_to_string(self, list):
        pass

    @abstractmethod
    def convert_from_string(self, string):
        pass