
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
        print( "Taak nummer:", taak['nummer'])
        print("Taak naam:" + " " + taak['naam'])
        print("Taak beschrijving:" + " " + taak['beschrijving'])
        print("Taak afgerond:", taak['afgerond'])
        print("====================================================")


def taak_verwijderen():
        taak_nummer_verwijder = int(input("Voer het taaknummer in dat je wilt verwijderen: "))

        gevonden = False
        for taak in taken_lijst:
            if taak["nummer"] == taak_nummer_verwijder:
                taken_lijst.remove(taak)
                print("Taak verwijderd.")
                gevonden = True
                break  # stoppen zodra de juiste taak is gevonden en verwijderd

        if not gevonden:
            print("Taak met dat nummer niet gevonden.")


def taak_afgerond():
    taak_afronden = int(input("Voer de taaknummer in die je wilt afronden"))

    for taak in taken_lijst:
        if taak['nummer'] == taak_afronden:
            taak['afgerond'] = True
        else:
            print("De genoemde taak is niet af te ronden")

def main():

 programma_draait = True

 while programma_draait:
     print("1 Bekijk taak")
     print("2 Voeg taak toe")
     print("3 Verwijder taak")
     print("4 Vink taak af")
     print("5 Stop")
     print("=============================================")

     gebruiker_input = int(input("Vul je invoer in"))

     if gebruiker_input == 1:
         taken_bekijken()
     if gebruiker_input == 2:
         taak_aanmaken()
     if gebruiker_input == 3:
         taak_verwijderen()
     if gebruiker_input == 4:
         taak_afgerond()
     if gebruiker_input == 5:
         programma_draait = False

if __name__ == '__main__':
    main()