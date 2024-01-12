from repository.KundeRepo import KundeRepo
from repository.GetränkRepo import GetränkRepo
from repository.GekochterGerichtRepo import GekochterGerichtRepo
from repository.BestellungRepo import BestellungRepo


def ShowData(Type):
    types = {
        0: GekochterGerichtRepo('gekochtergericht.dat'),
        1: GetränkRepo('getrank.dat'),
        2: KundeRepo('kunde.dat'),
        3: BestellungRepo('bestellung.dat')
    }

    repo = types[Type]

    list = repo.load()
    if list:
        for idx in range(len(list)):
            print(idx, str(list[idx]))

    print('\n')