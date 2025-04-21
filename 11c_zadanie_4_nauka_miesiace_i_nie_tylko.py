import random

POWITANIE = """
---------------------------------------------
-                                           -
-  witam w programie do nauki misiace       -
-                                           -
-  by Erni v.1.0.0            2023-03-26    -
-                                           -
---------------------------------------------
"""

POZEGNANIE ="""
---------------------------------------------
-                   Koniec                  -
-  by Erni v.1.0.0            2023-03-26    -
---------------------------------------------
"""



LENA_MIESIACE_RZYMSKIE = [
                            ("napisz rzymskimi ", "Styczen", "I"),
                            ("napisz rzymskimi ", "Luty", "II"),
                            ("napisz rzymskimi ", "Marzec", "III"),
                            ("napisz rzymskimi ", "Kwiecien", "IV"),
                            ("napisz rzymskimi ", "Maj", "V"),
                            ("napisz rzymskimi ", "Czerwiec", "VI"),
                            ("napisz rzymskimi ", "Lipiec", "VII"),
                            ("napisz rzymskimi ", "Sierpien", "VIII"),
                            ("napisz rzymskimi ", "Wrzesien", "IX"),
                            ("napisz rzymskimi ", "Pazdziernik", "X"),
                            ("napisz rzymskimi ", "Listopad", "XI"),
                            ("napisz rzymskimi ", "Grudzień", "XII"),
                          ]

LENA_ILE_DNI_MA_MIESIAC = [
                            ("ile dni ma ", "Styczen", "31"),
                            ("ile dni ma ", "Luty", "28"),
                            ("ile dni ma ", "Marzec", "31"),
                            ("ile dni ma ", "Kwiecien", "30"),
                            ("ile dni ma ", "Maj", "31"),
                            ("ile dni ma ", "Czerwiec", "30"),
                            ("ile dni ma ", "Lipiec", "31"),
                            ("ile dni ma ", "Sierpien", "31"),
                            ("ile dni ma ", "Wrzesien", "30"),
                            ("ile dni ma ", "Pazdziernik", "31"),
                            ("ile dni ma ", "Listopad", "30"),
                            ("ile dni ma ", "Grudzień", "31"),
]

LENA_ZAPISZ_DATE = [
                            ("napisz miesiac rzymskimi", "1.04", "7 IV"),
                            ("napisz miesiac rzymskimi", "7.09", "7 IX"),
                            ("napisz miesiac rzymskimi", "24.06", "24 VI"),
                            ("napisz miesiac rzymskimi", "1.05", "1 V"),
                            ("napisz miesiac rzymskimi", "24.12", "24 XII"),
                            ("napisz miesiac rzymskimi", "1.01", "1 I"),
                            ("napisz miesiac rzymskimi", "1 czerwca", "1 VI"),
                    ]


zadania_count = 20
poprawne = 0
blendne = 0

def sprawdz_ucznia(SLOWA_LISTA):
    global blendne
    global poprawne
    ilosc_elementow=len(SLOWA_LISTA)
    x=random.randint(0, ilosc_elementow - 1)
    element=SLOWA_LISTA[x]
    pytanie   = element[0]
    zadanie   = element[1]
    odpowiedz = element[2]

    odpowiedz_ucznia = input(pytanie + " " + zadanie + " ? : ")
    if (odpowiedz.upper()==odpowiedz_ucznia.upper()):
        print("OK :)")
        poprawne = poprawne + 1
    else:
        print(f"Nie, poprawna odpowiedz to: ", odpowiedz)
        blendne = blendne + 1

def wybrana_lista():
    print("Wybiesz  zestaw zadan:")
    print("1 - LENA_MIESIACE_RZYMSKIE np. grudzien -> XII")
    print("2 - LENA_ILE_DNI_MA_MIESIAC np. grudzien -> 31")
    print("3 - LENA_ZAPISZ_DATE np. 1.01 -> 01 I")
    print("4 - LENA mieszkane zadania z datami")

    odpowiedz = int(input(f"podaj numer zestawu : "))
    print(odpowiedz)
    if (odpowiedz == 1): return LENA_MIESIACE_RZYMSKIE
    if (odpowiedz == 2): return LENA_ILE_DNI_MA_MIESIAC
    if (odpowiedz == 3): return LENA_ZAPISZ_DATE
    if (odpowiedz == 4): return LENA_ZAPISZ_DATE + LENA_ILE_DNI_MA_MIESIAC + LENA_MIESIACE_RZYMSKIE



    print("niepoprawny numer za kare masz liste Ernesta")
    return LENA_MIESIACE_RZYMSKIE



print(POWITANIE)
lista = wybrana_lista();

for i in range(zadania_count):
    print("")
    print(f"zadanie {i+1}:")
    sprawdz_ucznia(lista)



print("")
print("Odpowiedzi złe   : ",blendne)
print("Odpowiedzi dobre : ",poprawne)
print(f"Twoj wynik to    : {poprawne}/{zadania_count}")
print("")
print(POZEGNANIE)
print(f"pa pa")
print(f"Have a nice day.")

input("press enter")

#if zadania_count == 10:
#questions_count += 1
#poprawne = poprawne+1
#blendne = blendne+1