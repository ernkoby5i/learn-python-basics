import random

import random
from math import pi
from math import sqrt as pierwiastek

POWITANIE = """
---------------------------------------------
-                                           -
-  witam w programie do nauki angielskiego  -
-                                           -
-  by Ernest v.1.0.0          2022-12-03    -
-                                           -
---------------------------------------------
"""

POZEGNANIE ="""
------------
-  Koniec  -
-  pa  pa  -
------------
"""

LISTA_ERNESTA = [("krowa", "cow"),
               ("kot", "cat"),
               ("ryba", "fish"),
               ]
LISTA_LENY = [("pada snmieg", "snowing"),
               ("pada", "raining"),
               ("zimny", "cold"), ("goracy", "hot"),  ("plaszcz", "coat"), ("czapka", "hat"),
               ]


def sprawdz_ucznia(SLOWA_LISTA):
    ilosc_elementow=len(SLOWA_LISTA)
    x=random.randint(0, ilosc_elementow -1)
    element=SLOWA_LISTA[x]
    wyraz_pl=element[0]
    wyraz_en=element[1]

    odpowiedz = input(f"jak jest po angielsku {wyraz_pl} : ")
    if (wyraz_en==odpowiedz):
        print("BRAWO!:)")
    else:
        print(f"poprawna odpowiedz to", wyraz_en)
    #print(x, SLOWA_LISTA[x], element, wyraz_pl, wyraz_en, odpowiedz)


print(POWITANIE)
imie = input("imie gracza [Lena, Ernest]:")

for i in range(10):
    print("")
    print(f"zadanie {i+1}:")
    sprawdz_ucznia(LISTA_LENY)

print(POZEGNANIE)



