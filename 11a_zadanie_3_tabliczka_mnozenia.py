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


# 2 liczby a,b takie ze wynik mnozenia 10 < wynik < 30
def wylosuj_liczby_a_i_b():
    a = 0
    b = 0
    while True:
        a = random.randint(2, 10)
        b = random.randint(2, 10)
        wynik_mnorzenia = a * b
        if ((wynik_mnorzenia <= 30) and (wynik_mnorzenia > 10)):
            break
    return (a,b)

def sprawdz_ucznia(nr_zadania, a, b):
    print("")
    odpowiedz = int(input(f"zadanie {nr_zadania} - podaj wynik {a} * {b} = "))
    if (odpowiedz == a * b):
        print("BRAWO!:)")
        return True
    else:
        print(f"Zła odpowiedz :(. poprawny wynik to:  {a} * {b} = {a * b}")
        return False


print("-----------------------------------------")
print("-                                       -")
print("-  witam w programie do nauki mnozenia  -")
print("-                                       -")
print("-  by Ernest                            -")
print("-----------------------------------------")

questions_count = 0
correct = 0
incorrect = 0

while True:
    if questions_count == 10:
        break
    questions_count += 1
    (a, b) = wylosuj_liczby_a_i_b()
    odpowiedz_jest_prawidlowa = sprawdz_ucznia(questions_count, a, b)

    if odpowiedz_jest_prawidlowa:
        correct = correct+1
    else:
        incorrect = incorrect+1

print("")
print("złe",incorrect)
print("Dobre",correct)
print(f"Twoj wynik to: {correct}/{questions_count}")
print("")
print("------------")
print("-  Koniec  -")
print("------------")

