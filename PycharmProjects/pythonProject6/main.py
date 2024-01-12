# 1
def entfernen_duplik(number_list):          # Wir definieren eine Funktion
    unique_numbers = []                     # man macht eine leere Liste
    for number in number_list:              # wir durchgehen alle Elemente aus number_list
        if number not in unique_numbers:    # man obersucht ob der Nummer schon in unique_numbers existiert
            unique_numbers.append(number)   # diesen Reihe uberpruft ob man in der Liste dies Nummer schon existiert
    return unique_numbers                   # man returniert alle unique_numbers

input_list = [11, 22, 11, 34, 22, 45, 34]
unique_numbers = entfernen_duplik(input_list)
print("Liste ohne Duplikate:", unique_numbers)

#2
def anz_symm(list):                         # man definiert eine Funktion
    ct=0                                    # ct bekommt den Wert 0
    for e in range(len(list)):              # man geht durch alle Elemente
        for i in range(e+1,len(list)):      # Diese Reihe stellt sicher, dass dieses Element mit jedem darauffolgenden Element gesichert wird
            x = list[i]%10                  # man rechnet die letzte Ziffer des Elementes
            if list[e] == list[i]//10 + x*10: # Bei dieser Prüfung wird die erste Ziffer der ersten Zahl mit der letzten Ziffer der zweiten Zahl verglichen.
                ct+=1                       # wenn die oberen Zustande wahr sind, wird ct steigen
    return ct                               # ct wird returniert

input_list = [11, 43, 43, 22, 33, 34, 44, 54]
count = anz_symm(input_list)
print("Anzahl der symmetrischen Paare:", count)

#3
def konk(list):
    l=[]                        # se creeaza o lista goala
    number=''                   # se creeaza un sir gol
    for e in list:              # parcurgem fiecare element din lista e
        e=str(e)                # elementul e este transformat intr un sir de caractere pt a parcurge cifrele individuale
        for i in e:             # se parcurg cifrele individuale ale sirului
            if i not in l:      # se verifica daca cifra i nu este in lista 1
                l.append(int(i))    # daca nu este in lista, este adaugata ca un nr intreg
    l.sort(reverse=True)        # lista este sortata in ordine descrescatoare
    for idx in l:               # se prcurge fiecare cifra din lista sortata
        idx=str(idx)            # cifra este transformata intr un sir de caractere
        number+=idx             # cifra este adaugata la sirul number
    return int(number)          # se returneaza numarul rezultat

input_list = [45, 12, 78, 34]
result = konk(input_list)
print("Größte Zahl:", result)
#4
def crypt1(list):                   # definim o functie
    key = list[0]                   # initializam o variabila
    for e in range(1, len(list)):   # parcurgem fiecare element
        list[e]+= key               # si adaugam valoarea in key la fiecare el.
    return list                     # returnam lista modificata

def crypt2(list):                   # initializam o functie, care primeste o lista
    key = list[0]                   # initializam o variabila, cu prima valoarea din lista
    for e in range(1, len(list)):   # parcurgem elementele din lista
        list[e]*= key               # inmultim fiecare element cu valoarea stocata
    return list                     # returnam lista

def crypt3(list):                   # functia primeste o lista
    key = list[0]                   # initializam prima valoare cu variabila 'key'
    for e in range(1, len(list)):   # parcurgem toate elementele
        list[e]^= key               # adaugam operatia ˆ intre fiecare elemente
    return list                     # la final returnam lista modificata

input_list = [5, 10, 15, 20, ]
result1 = crypt1(input_list)
result2 = crypt2(input_list)
result3 = crypt3(input_list)

print("Ergebnis nach crypt1:", result1)
print("Ergebnis nach crypt2:", result2)
print("Ergebnis nach crypt3:", result3)

# 5
def main():
    entfernen_duplik()
    anz_symm()
    konk()
    crypt1()
    crypt2()
    crypt3()
    main()



