# program do nauki tabliczki monozenia
# Phase 1:
#  skorzystaj z random ktora miales w module math
#  a = wylosuj liczbe z zakresu 2..10
#  b = wylosuj liczbe z zakresu 2..10
#  wypisz przy pomocy print obie liczby
#  wczytaj liczbe odpowiedz uzywajac input
#  sprawdz czy a x b == odpowiedz przy pomocy if
#  jezeli prawqda wupisz BRAWO :) a jezeli falsz wypisz SLABO :(

# Phase 2:
#  zamien powyzszy kod na funkcje mnozenie_odpowiedz_prawidlowa()
#  def zadanie_rozwiazane_prawidlowo():
#  funkcja zwraca:
#     True jezeli odpowiedzi poprawna
#     False jezeli odpowiedz bledna
#  uruchom funkcje w petli 10 razy


# Phase 3:
#  wykorzystaj 2 zmienne:
#  ilosc_poprawne - zawiera ilosc poprawnych odpowidzi. zwieksz za kazdym razem kiedy odpowiedz poprawan
#  ilosc_pytan    - zawiera ilosc zadanych pytan.
#  po zebraniou odpowiedzi wypisz na ekranie przy pomocy print
#  "udzieloneo 2 poprawnych odpowiedzi na 10 pytan: 2/10"

import random

import random
from math import pi
from math import sqrt as pierwiastek


i = 0

while True:
    if i >= 10:
        break

    a = random.randint(2, 10)
    b = random.randint(2, 10)

    wynik_mnorzenia = a * b
    if (wynik_mnorzenia <= 30):
        i += 1
        odpowiedz = int(input(f"zadanie {i} - podaj wynik {a} * {b} = "))
        if (odpowiedz == a * b):
            print("BRAWO!:)")
        else:
            print("Zła odpowiedz")
            print("Wynik mnorzenia", wynik_mnorzenia)

print("Koniec")

