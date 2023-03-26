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



LENA_MIESIACE_RZYMSKIE = [  ("Styczen", "I"), ("Luty", "II"),
                    ("Marzec", "III"), ("Kwiecien", "IV"),
                    ("Maj", "V"), ("Czerwiec", "VI"),
                    ("Lipiec", "VII"), ("Sierpien", "VIII"),
                    ("Wrzesien", "IX"),
                    ("Pazdziernik", "X"),
                    ("Listopad", "XI"),
                    ("Grudzień", "XII"),
                    ("7.09", "7 XIX"),
                    ("24.06", "24 VI"),
                    ("1.05", "1 V"),
                    ("24.12", "24 XII"),
                    ("1.01", "1 I"),
                    ("1 czerwca", "1 VI"),
                    ]

LISTA_ERNESTA = [("wiosna", "spring"), ("lato", "summer"), ("jesień", "autumn"), ("zima", "winter")]

zadania_count = 10
poprawne = 0
blendne = 0

def sprawdz_ucznia(SLOWA_LISTA):
    global blendne
    global poprawne
    ilosc_elementow=len(SLOWA_LISTA)
    x=random.randint(0, ilosc_elementow -1)
    element=SLOWA_LISTA[x]
    pytanie=element[0]
    odpowiedz=element[1]

    odpowiedz_ucznia = input(f"jak bedzie '{pytanie}' ? : ")
    if (odpowiedz==odpowiedz_ucznia):
        print("OK :)")
        poprawne = poprawne + 1
    else:
        print(f"Nie, poprawna odpowiedz to: ", odpowiedz)
        blendne = blendne + 1

def wybrana_lista():
    print("Wybiesz jedna liste")
    print("0 - LISTA_ERNESTA pory roku")
    print("1 - LENA_MIESIACE_RZYMSKIE np. grudzien -> XII")

    odpowiedz = int(input(f"podaj numer zestawu : "))
    print(odpowiedz)
    if (odpowiedz == 0):return LISTA_ERNESTA
    if (odpowiedz == 1): return LENA_MIESIACE_RZYMSKIE



    print("niepoprawny numer za kare masz liste Ernesta")
    return LISTA_ERNESTA



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