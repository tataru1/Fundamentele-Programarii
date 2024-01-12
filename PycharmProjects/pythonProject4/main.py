# Exercitiu 9 a

def prime_fact(n):
    fact = []                   # Hier werden die Primfaktoren gespeichert
    divis = 2                   # Der kleinste Primfaktor

    while divis <= n:           # Bis divis kleiner als n ist
        if n % divis == 0:      # Wenn n mod divis 0 ist
            fact.append(divis)  
            n //= divis
        else:
            divis += 1

    return fact

# Beispiel
number = 100
fact = prime_fact(number)
print(f"Die Primfaktorzerlegung von {number} ist: {fact}")

# 9 b
def langste_aufeinand_folge(numbers):   # se defineste functia, care primeste un vector de numere
    if not numbers:                     # verificam daca vectorul e gol
        return []                       # verificam o lista goala daca e gol vectorul

    aktuell_folge = [numbers[0]]        # initializam o lista, care retine pozitia actuala
    langste_folge = [numbers[0]]        # initializam o lista care retine cea mai lunga secventa

    for i in range(1, len(numbers)):    # trecem prin vector incepand de la al 2-lea element
        if numbers[i] % 10 == numbers[i - 1] % 10:  # verificam daca uc a elementului curent este egala cu uc a elementului precedent
            aktuell_folge.append(numbers[i])
        else:
            if len(aktuell_folge) > len(langste_folge): # daca nu au acelasi uc, verificam daca secventa curenta, este mai mare dact cea mai lunga secventa
                langste_folge = aktuell_folge           # daca da, cea mai lunga secventa preia valoarea secventei curente
            aktuell_folge = [numbers[i]]                # secventa curenta este reinitializata

    if len(aktuell_folge) > len(langste_folge):         # verificam din nou daca secventa actuala este mai mare decat cea mai lunga secventa
        langste_folge = aktuell_folge                   # daca este schimbam valoarea

    return langste_folge                                # returnam cea mai lunga secventa

# Beispiel
number_vector = [12, 212, 23, 34, 45, 56, 67, 78, 89, 90, 91, 10, 11]

langste_folge = langste_aufeinand_folge(number_vector)
print("Die längste aufeinanderfolgende Teilfolge ist:", langste_folge)

def main():
    prime_fact()
    langste_aufeinand_folge()
