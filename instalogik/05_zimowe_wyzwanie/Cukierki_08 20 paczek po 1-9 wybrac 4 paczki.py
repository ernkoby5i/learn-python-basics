"""
Program 8.
W cukierni jest 20 paczek cukierków, a w każdej z nich jest od 1 do 9 cukierków.
Napisz program, który po podaniu liczby cukierków w każdej z paczek,
obliczy ile najwięcej cukierków można otrzymać wybierając 4 paczki.
"""

"""
Metoda:

SPOSOB 1: - ZLY
zapisujemy w pamieci ilosc paczek z liczba cukierokwo np.
A - paczki po 9 
B - paczki po 8 
C - paczki po 7
D - paczki po 6 
E - paczki po 5
F - paczki po 4
G - paczki po 3
H - paczki po 2
I - paczki po 1

ale nie mamy tyle komorek. 
wiec mozemy upakowac w jednej zmiennej.

SPOSOB 2: - ZLY 
    A - 20 20 20 - 9 8 7  
    B - 20 20 20 - 6 5 4
    C - 20 20 20 - 3 2 1

    - if 9 then A = A + 1 00 00
    - if 8 then A = A +    1 00
    - if 7 then A = A +       1

nastepjnie zmnniejszamy zmienne A,B,C i dodajemy za kazdym razem odpowiednia ilosc do D
ale .... nie mamy zmiennej ktora mozna wykorzystac do petli. 

------------------------------------------------------------
-    NASZE ROZWIZANIE NR 3.
------------------------------------------------------------

--- zapizanie informacji o paczkach ---

SPOSOB 3: - DOBRY 
    A - informacja o 9..6 (4)
    B - informacja o 5..2 (4)
    C - informacja 0    1 (1) oraz licznick counter na ostatniej pozycji

aby zapisac na A informacjeo na temat 4 paczek 
skorzystamy z faktu ze do zapisu 20 wystarczy nam 5 bit'ow 11111 
20 - binarnie 10100 
zatem 4 cyfry zapisane w ten sposob to: 10100 10100 10100 10100 = 676500 < 999 999 - bingo

    if (D == 9): A = A + 32768
    if (D == 8): A = A + 1024
    if (D == 7): A = A + 32
    if (D == 6): A = A + 1

czyli C = 3 00 19 -> znaczy ze mamy jeszcze 19 paczek po "1" a brakuje nam 3 cukierok.
w praktyce moze to byc przypadek

--- koniec zapisywania informacji o paczkach ---   

bedziemy najpierw zabierac z A:
WEZ_NATSEPNA_PACZKE:  
  if A >= 32768 then  D = D + 9; goto WEZ_NATSEPNA_PACZKE
  if A >= 1024  then  D = D + 8; goto WEZ_NATSEPNA_PACZKE
  ...
  if B >= 32  then  D = D + 3; goto WEZ_NATSEPNA_PACZKE
  if B >= 1   then  D = D + 2; goto WEZ_NATSEPNA_PACZKE
  
  # jezeli tutaj dotarlismy to znaczy ze nie ma juz ani jednej paczki po 2..9 
  # wiec musmiy wziac paczke z C o ilosci "1"
  # jednoczenise w C mamy info ile paczek nam prakuje. 
  # np. byly tylko 19 po "1' wtedy C = 20 00 00 (licznik 20) + 19 paczek po "1" 
  # C = 200019
  WEZ z OSTATNIEJ PACZKI:
  C := C - 10000 # zmniejsz licznik
  C := C - 1     # zabierz paczke "1"
  D := D + 1     # dodaj liczbe cukierkow (1) do D
  WEZ_NATSEPNA_PACZKE
  
  
KONIEC
    
  
  
  

itd.  


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

