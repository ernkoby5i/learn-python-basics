"""
Program 8. W cukierni jest 20 paczek cukierków, a w każdej z nich jest od 1 do 9 cukierków.
Napisz program, który po podaniu liczby cukierków w każdej z paczek,
obliczy ile najwięcej cukierków można otrzymać wybierając 4 paczki.
"""

import random
lista = []
#test_lista = [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

A = 0
B = 0
C = 0
D = 0

C = 500000
i = 50
while C >= 10000:
    C = C - 10000
    i = i - 1

    D = random.randint(1, 50)
    #D = test_lista[i-1]
    lista.append(D)

    if (D == 8): A = A + 10000
    if (D == 7): A = A + 100
    if (D == 6): A = A + 1


    if (D == 5): B = B + 10000
    if (D == 4): B = B + 100
    if (D == 3): B = B + 1

    if (D == 2): C = C + 100
    if (D == 1): C = C + 1

print(A, B, C)
D = 0

paczki = []

C = C + 80000
while C >= 10000:
    C = C - 10000

    paczki.append(1)
    continue



lista.sort(reverse=True)
print("LISTA : ",  lista)
print(f"suma 4 elementow {lista[0:4]} = {sum(lista[0:4])}")

print(f"Wybrano paczki {paczki}. SUMA = {sum(paczki)}")

