"""
Program 8. W cukierni jest 20 paczek cukierków, a w każdej z nich jest od 1 do 9 cukierków.
Napisz program, który po podaniu liczby cukierków w każdej z paczek,
obliczy ile najwięcej cukierków można otrzymać wybierając 4 paczki.
"""

import random
lista = []
test_lista = []
for i in range(20):
    test_lista.append(random.randint(1, 9))

test_lista = [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


A = 0
B = 0
C = 0
D = 0

C = 200000
i = 20
while C >= 10000:
    C = C - 10000
    i = i - 1

    D = random.randint(1, 9)
    D = test_lista[i-1]
    lista.append(D)

    if (D == 9): A = A + 32768
    if (D == 8): A = A + 1024
    if (D == 7): A = A + 32
    if (D == 6): A = A + 1

    if (D == 5): B = B + 32768
    if (D == 4): B = B + 1024
    if (D == 3): B = B + 32
    if (D == 2): B = B + 1

    if (D == 1): C = C + 1

print(A, B, C)
D = 0

paczki = []

C = C + 40000
while C >= 10000:
    C = C - 10000
    if A >= 32768:
        paczki.append(9)
        D = D + 9
        A = A - 32768
        continue
    if A >= 1024:
        paczki.append(8)
        D = D + 8
        A = A - 1024
        continue
    if A >= 32:
        paczki.append(7)
        D = D + 7
        A = A - 32
        continue
    if A >= 1:
        paczki.append(6)
        D = D + 6
        A = A - 1
        continue

    if B >= 32768:
        paczki.append(5)
        D = D + 5
        B = B - 32768
        continue
    if B >= 1024:
        paczki.append(4)
        D = D + 4
        B = B - 1024
        continue
    if B >= 32:
        paczki.append(3)
        D = D + 3
        B = B - 32
        continue
    if B >= 1:
        paczki.append(2)
        D = D + 2
        B = B - 1
        continue

    paczki.append(1)
    D = D + 1
    C = C - 1
    continue



lista.sort(reverse=True)
print("LISTA : ",  lista)
print(f"suma 4 elementow {lista[0:4]} = {sum(lista[0:4])}")

print(f"Wybrano paczki {paczki}. SUMA = {sum(paczki)}")

