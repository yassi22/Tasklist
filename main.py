
taken_lijst = []


def taak_aanmaken():
    taak_nummer = int(input("Voer een taak nummer in"))
    taak_naam = input("Voer je taak naam in")
    taak_beschrijving = input("Voer een beschrijving in")
    taak_afgerond = False

    taak = {
        "nummer" : taak_nummer,
        "naam" : taak_naam,
        "beschrijving" : taak_beschrijving,
        "afgerond" : taak_afgerond
    }

    taken_lijst.append(taak)


def taken_bekijken():
    for taak in taken_lijst:
        print( "Taak nummer", taak['nummer'])
        print("Taak naam" + " " + taak['naam'])
        print("Taak beschrijving" + " " + taak['beschrijving'])
        print("Taak afgerond", taak['afgerond'])


def taak_verwijderen():
    taak_positie_verwijder = int(input("Voer de taak nummer die je wilt verwijderen"))

    taken_lijst.remove(taak_positie_verwijder)


def main():
 taak_aanmaken()
 taken_bekijken()
 taak_verwijderen()

if __name__ == '__main__':
    main()