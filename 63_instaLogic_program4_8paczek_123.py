# mamy 8 paczek
# w kazde 1,2 lub 3
# wybieramy 4 paczki zeby bylo najwiecej

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






















