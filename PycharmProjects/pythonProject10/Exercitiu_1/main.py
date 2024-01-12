from letters import *
def menu():
    print("""
    W - der Stift bewegt sich um 10 Pixel vorwarts
    S - der Stift bewegt sich um 10 pixel ruckwarts
    D - der Stift bewegt sich um 45 Grad nach rechts
    A - der Stift bewegt sich um 45 Grad nach links
    F - hebt den Stift nach oben
    G - legt den Stift wieder ab
    Space - Exit
    """)

def main():
    f = open("Datei.txt", 'w')
    while True:
        menu()
        Buchstabe = input('Command:')
        if Buchstabe == 'w':
            W()
            f.write('w')

        if Buchstabe == 's':
            S()
            f.write('s')

        if Buchstabe == 'd':
            D()
            f.write('d')

        if Buchstabe == 'a':
            A()
            f.write('a')

        if Buchstabe == 'f':
            F()
            f.write('f')

        if Buchstabe == 'g':
            G()
            f.write('g')

        if Buchstabe == ' ':
            break

    f.close()
    f = open("Datei.txt", 'r')

main()
