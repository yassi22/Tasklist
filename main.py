
taken_lijst = []


def taak_aanmaken():
    taak_naam = input("Voer je taak naam in")
    taak_beschrijving = input("Voer een beschrijving in")
    taak_afgerond = False

    taak = {
        "naam" : taak_naam,
        "beschrijving" : taak_beschrijving,
         "afgerond" : taak_afgerond
    }

    taken_lijst.append(taak)


def taken_bekijken():
    for taak in taken_lijst:
        print(taak['naam'])
        print(taak['beschrijving'])
        print(taak['afgerond'])


def main():
 taak_aanmaken()
 taken_bekijken()


if __name__ == '__main__':
    main()