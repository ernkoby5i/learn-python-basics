A = 0
B = 0
C = 0
D = 0

C = 11

#for i in range(4):
while C > 0:
    C = C -1
    D = int(input("podaj liczbe cukierkow : "))
    print(f"D = {D}")

    if(D>A):
        B = A
        A = D
        continue
    if(B<D):
        A = A
        B = D

print(f"Suma Cukierkow A={A}, B={B}, SUMA = {A+B}")

















