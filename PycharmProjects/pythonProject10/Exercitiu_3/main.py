import random


def citeste_desene_din_fisier(nume_fisier):
    desene = {}
    with open(nume_fisier, 'r') as file:
        linii = file.read().split('\n\n')
        for linie in linii:
            if linie:
                cheie, valoare = linie.split('\n', 1)
                desene[cheie] = valoare
    return desene


def afiseaza_desen(opțiune):
    return desene[opțiune]


def joaca_piarta_hartie_foarfeca():
    scor_utilizator = 0
    scor_computer = 0
    optiuni = ['piatra', 'hartie', 'foarfeca']

    for _ in range(3):  # Joaca cel mai bun din 3 meciuri
        print("Alege: piatra, hartie sau foarfeca")
        alegere_utilizator = input().lower()
        alegere_computer = random.choice(optiuni)

        print("\nAlegerea ta:")
        print(afiseaza_desen(alegere_utilizator))
        print("\nAlegerea computerului:")
        print(afiseaza_desen(alegere_computer))

        if alegere_utilizator == alegere_computer:
            print("Egalitate!")
        elif (alegere_utilizator == 'piatra' and alegere_computer == 'foarfeca') or \
                (alegere_utilizator == 'hartie' and alegere_computer == 'piatra') or \
                (alegere_utilizator == 'foarfeca' and alegere_computer == 'hartie'):
            print("Ai câștigat acest meci!")
            scor_utilizator += 1
        else:
            print("Computerul a câștigat acest meci!")
            scor_computer += 1

    print("\nScor final:")
    print(f"Utilizator: {scor_utilizator} - Computer: {scor_computer}")

    if scor_utilizator > scor_computer:
        print("Felicitări! Ai câștigat!")
    elif scor_utilizator < scor_computer:
        print("Ai pierdut. Mai încercăm data viitoare!")
    else:
        print("Egalitate!")

desene = citeste_desene_din_fisier("alegere.txt")
joaca_piarta_hartie_foarfeca()