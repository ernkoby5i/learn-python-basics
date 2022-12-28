A = 0
B = 0
C = 0
D = 0



for i in range(4):
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

















