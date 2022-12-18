import random

import random
from math import pi
from math import sqrt as pierwiastek

POWITANIE = """
---------------------------------------------
-                                           -
-  witam w programie do nauki angielskiego  -
-                                           -
-  by Erni v.1.0.0            2022-12-03    -
-                                           -
---------------------------------------------
"""

POZEGNANIE ="""
---------------------------------------------
-                   Koniec                  -
-  by Erni v.1.0.0            2022-12-03    -
---------------------------------------------
"""

LISTA_LENY_0 = [("owca", "sheep"), ("kaczka", "duck"),
              ("krowa", "cow"), ("kura", "hen"),
              ("kon", "horse"), ("kot", "cat"),
              ("koza", "goat"), ("kurczak", "chick"),
              ("cielak", "calf"), ("zrebak", "foal"),
              ("mala owieczka - jagnie", "lamb"),
              ("kaczuszka", "duckling"), ("kotek maly", "kitten")
               ]

LISTA_LENY_1 = [("pada snieg", "snowing"), ("pada descz", "raining"),
              ("zimny", "cold"), ("goracy", "hot"),
              ("plaszcz", "coat"), ("czapka", "hat"),
              ("koszulka", "t-shirt"), ("sweter", "jumper"),
              ("spodnie", "trousers"), ("spodenki", "shorst"),
              ("sukienka", "skirt"),
              ("słoneczny", "sunny"), ("pochmurny", "cloudy"),
              ("wiosna", "spring"), ("lato", "summer"), ("jesień", "autumn"), ("zima", "winter"),
               ]

LISTA_LENY_2 = []


def sprawdz_ucznia(SLOWA_LISTA):
    ilosc_elementow=len(SLOWA_LISTA)
    x=random.randint(0, ilosc_elementow -1)
    element=SLOWA_LISTA[x]
    wyraz_pl=element[0]
    wyraz_en=element[1]

    odpowiedz = input(f"jak jest po angielsku '{wyraz_pl}' ? : ")
    if (wyraz_en==odpowiedz):
        print("BRAWO!:)")
    else:
        print(f"poprawna odpowiedz to: ", wyraz_en)
    #print(x, SLOWA_LISTA[x], element, wyraz_pl, wyraz_en, odpowiedz)




print(POWITANIE)
imie = input("imie gracza [Lena, Ernest]:")

for i in range(5):
    print("")
    print(f"zadanie {i+1}:")
    if(imie=="Lena"):
        sprawdz_ucznia(LISTA_LENY)
    else:
        sprawdz_ucznia(LISTA_ERNESTA)

print(POZEGNANIE)
print(f"pa pa, {imie}.")
print(f"Have a nice day.")

input("press enter")



