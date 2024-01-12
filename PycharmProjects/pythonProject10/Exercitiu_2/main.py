def inlocuieste_cuvinte(cale_fisier, cuvant_de_inlocuit, cuvant_inlocuitor):
    try:
        with open(cale_fisier, 'r', encoding='utf-8') as fisier:
            continut = fisier.read()

        numar_inainte = continut.lower().count(cuvant_de_inlocuit.lower())

        continut_inlocuit = continut.replace(cuvant_de_inlocuit, cuvant_inlocuitor, -1)

        with open(cale_fisier, 'w', encoding='utf-8') as fisier:
            fisier.write(continut_inlocuit)

        numar_dupa = continut_inlocuit.lower().count(cuvant_inlocuitor.lower())

        numar_inlocuiri = min(numar_inainte, numar_dupa) if isinstance(numar_dupa, int) else 0

        if numar_inlocuiri > 0:
            print(f"S-a inlocuit '{cuvant_de_inlocuit}' cu '{cuvant_inlocuitor}' in {numar_inlocuiri} locuri.")
        else:
            print(f"Cuvantul '{cuvant_de_inlocuit}' nu a fost gasit in fisier.")

    except FileNotFoundError:
        print("Fisierul specificat nu a fost gasit.")
    except Exception as e:
        print(f"A intervenit o eroare: {e}")

cale_fisier = input("Pfad zur Datei: ")
cuvant_de_inlocuit = input("Wort zu ersetzen: ")
cuvant_inlocuitor = input("Ersatzwort: ")

inlocuieste_cuvinte(cale_fisier, cuvant_de_inlocuit, cuvant_inlocuitor)