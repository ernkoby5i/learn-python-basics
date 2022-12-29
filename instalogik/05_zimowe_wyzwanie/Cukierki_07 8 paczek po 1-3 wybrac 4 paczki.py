"""
Program 7.
W cukierni jest 8 paczek cukierków,
a w każdej z nich jest od 1 do 3 cukierków.
Napisz program, który po podaniu liczby cukierków w każdej z paczek,
obliczy ile najwięcej cukierków można otrzymać wybierając 4 paczki.
ROZWIAZANY
"""


A = 0
C = 8
D = 0


#for i in range(4):
while C > 0:
    C = C -1
    D = int(input("podaj liczbe cukierkow : "))

    if(D==3):
        A = A+100
    if(D==2):
        A = A+10
    if(D==1):
        A = A+1

print(A)

C=4
B=0
while C > 0:
    C = C - 1
    if(A >= 100):
        B=B+3
        A = A -100
        continue
    if(A >= 10):
        B = B+2
        A = A-10
        continue
    if(A>=1):
        B = B+1
        A = A-1
        continue
print(A)
print(B)


