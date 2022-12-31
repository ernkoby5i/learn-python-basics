"""
Program 10.
W cukierni jest 50 paczek cukierków, a w każdej z nich jest od 1 do 8 cukierków.
Napisz program, który po podaniu liczby cukierków w każdej z paczek,
obliczy ile najwięcej cukierków można otrzymać wybierając 8 paczek.
"""

"""
Rozwiazanie: 
zapiszemy tak: 
A - xx yy zz -> 8(xx), 7(yy), 6(zz)  
B - xx yy zz -> 5(xx), 4(yy), 3(zz)
C - nn yy zz ->   nn   2(yy), 1(zz) - gdzie nn to nasz licznik 

przyklad: 

A = 47 02 01 - 47 paczek po "8", 2 paczki po "7", 1 paczka po "6"
C =  8 12 13 - n  mamy dobrac 8 paczek, mamy jeszcze 12 po "2" i 13 po "1"

konsumyjemy najpier z A potem z B. 
i zmniejszamy licznik w C.

NA KONIEC
 
jezeli nic juz nam nie zosanie w A ani B (czyli A = 0 i B = 0)
a nasz licnzik n > 0 to znaczy ze musimy jeszcze wziac z paczek po "2" lub "1"

przeniesoiemny liczni do A po to aby latwiej bylo sprawdzac czy jeszcze sa paczki po 2
czli 
A = 0 
B = 0 
C = 8 12 13

musimy przniesc sobie 8 z C do A.
i doprowadzic do 
A = 8 
B = 0 
C = 12 13

no i dalej to tak jak wczesniej czyli:

:NEXT_PACZKA
while A>=1 then BEGIN
    A := A - 1 # zmniejsz licnzik 
    if C >= 100 then 
          C := C - 1     # zabierz paczke "2"
          D := D + 2     # dodaj liczbe cukierkow (2) do D
          GOTO :NEXT_PACZKA  
    if C >=   1 then 
          C := C - 1     # zabierz paczke "1"
          D := D + 1     # dodaj liczbe cukierkow (1) do D
          GOTO :NEXT_PACZKA 
END
   
 

"""

import random
lista = []
#test_lista = [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test_lista = []
for i in range(50):
    test_lista.append(random.randint(1, 9))

test_lista =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(len(test_lista))

A = 0
B = 0
C = 0
D = 0

C = 500000
i = 50
while C >= 10000:
    C = C - 10000
    i = i - 1

    D = random.randint(1, 8)
    D = test_lista[i-1]
    lista.append(D)

    if (D == 8): A = A + 10000
    if (D == 7): A = A + 100
    if (D == 6): A = A + 1


    if (D == 5): B = B + 10000
    if (D == 4): B = B + 100
    if (D == 3): B = B + 1

    if (D == 2): C = C + 100
    if (D == 1): C = C + 1

print("PO WCZYTANIU",A, B, C)
D = 0



paczki = []

C = C + 80000
while C >= 10000:

    if A >= 10000:
        paczki.append(8)
        D = D + 8
        A = A - 10000
        C = C - 10000
        continue
    if A >= 100:
        paczki.append(7)
        D = D + 7
        A = A - 100
        C = C - 10000
        continue
    if A >= 1:
        paczki.append(6)
        D = D + 6
        A = A - 1
        C = C - 10000
        continue

    if B >= 10000:
        paczki.append(5)
        D = D + 5
        B = B - 10000
        C = C - 10000
        continue

    if B >= 100:
        paczki.append(4)
        D = D + 4
        B = B - 100
        C = C - 10000
        continue
    if B >= 1:
        paczki.append(3)
        D = D + 3
        B = B - 1
        C = C - 10000
        continue
    break

print("PO ROZPISANIU 8-3",A,B,C, D)
while C >= 10000:
    C = C - 10000
    A = A + 10000

print(A,B,C)

while A >= 10000:
    if C >= 100:
        paczki.append(2)
        D = D + 2
        C = C - 100
        A = A - 10000
        continue
    if C >= 1:
        paczki.append(1)
        D = D + 1
        C = C - 1
        A = A - 10000
        continue
    break






lista.sort(reverse=True)
print("LISTA : ",  lista)
print(f"suma 8 elementow {lista[0:8]} = {sum(lista[0:8])}")

print(f"Wybrano paczki {paczki}. SUMA = {sum(paczki)}")

