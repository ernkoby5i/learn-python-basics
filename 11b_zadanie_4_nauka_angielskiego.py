import random

import random
from math import pi
from math import sqrt as pierwiastek

POWITANIE = """
---------------------------------------------
-                                           -
-  witam w programie do nauki angielskiego  -
-                                           -
-  by Erni v.1.1.0            2022-12-21    -
-                                           -
---------------------------------------------
"""

POZEGNANIE ="""
---------------------------------------------
-                   Koniec                  -
-  by Erni v.1.1.0            2022-12-21    -
---------------------------------------------
"""

LENA_CHAPTER_3 = [("kuchnia", "kitchen"), ("salon", "living room"),
                  ("sypialnia", "bedroom"), ("łazienka", "bathroom"),
                  ("toaleta", "toilet"), ("jadalnia", "dining room"),
                  ("hol", "hall"),
               ]

LENA_CHAPTER_2 = [("owca", "sheep"), ("kaczka", "duck"),
              ("krowa", "cow"), ("kura", "hen"),
              ("koń", "horse"), ("kot duży", "cat"),
              ("koza", "goat"), ("kurczak", "chick"),
              ("cielak", "calf"), ("źrebak", "foal"),
              ("mała owieczka - jagnie", "lamb"),
              ("mała kaczuszka", "duckling"), ("kotek mały", "kitten")
               ]

LENA_CHAPTER_1 = [("pada snieg", "snowing"), ("pada descz", "raining"),
              ("zimny", "cold"), ("goracy", "hot"),
              ("plaszcz", "coat"), ("czapka", "hat"),
              ("koszulka", "t-shirt"), ("sweter", "jumper"),
              ("spodnie", "trousers"), ("spodenki", "shorst"),
              ("sukienka", "skirt"),
              ("słoneczny", "sunny"), ("pochmurny", "cloudy"),
              ("wiosna", "spring"), ("lato", "summer"), ("jesień", "autumn"), ("zima", "winter"),
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
    wyraz_pl=element[0]
    wyraz_en=element[1]

    odpowiedz = input(f"jak jest po angielsku '{wyraz_pl}' ? : ")
    if (wyraz_en==odpowiedz):
        print("BRAWO!:)")
        poprawne = poprawne + 1
    else:
        print(f"poprawna odpowiedz to: ", wyraz_en)
        blendne = blendne + 1
    #print(x, SLOWA_LISTA[x], element, wyraz_pl, wyraz_en, odpowiedz)




print(POWITANIE)
lista = LISTA_ERNESTA
imie = input("imie gracza [Lena, Ernest]:")

if (imie == "Lena"):
    lista = LENA_CHAPTER_3
else:
    lista = LISTA_ERNESTA

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
print(f"pa pa, {imie}.")
print(f"Have a nice day.")

input("press enter")

#if zadania_count == 10:
#questions_count += 1
#poprawne = poprawne+1
#blendne = blendne+1