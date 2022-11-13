# Zadaie 2: Liczby pierwsze
# sprawdz czy liczna n jest liczba piwersza
# Step 1. sprawdz czy dzieli sie przez liczby od 2, n-1 jezeli tak to nie jest
#         uzyj for i range
# Step 2. zamien kod w funkcje ktora
# Step 3. znajdz liczby pierwsze 2 przedziale 1 .. 100


m=100

def czy_jest_pierwsza(n):
    print(" LICZBA : ", n , " PODZIELNIKEI ", end=' ')
    jest_Liczba_pierwsza = True
    for y in range(2, n):
        # print(n,"/", y,'=',n%y)
        if n % y == 0:
            # print(n,"podzielne przez", y)
            print(y, end=' ')
            jest_Liczba_pierwsza = False

    if jest_Liczba_pierwsza:
        print("PIERWSZA")
    else:
        print("NIE")
    return jest_Liczba_pierwsza

def czy_jest_pierwsza_rk(n):
    jest_Liczba_pierwsza = True
    for y in range(2, n):
        if n % y == 0:
            jest_Liczba_pierwsza = False
    if jest_Liczba_pierwsza:
        print("PIERWSZA:",n)
    return jest_Liczba_pierwsza





for y in range(500000, 650000):
    czy_jest_pierwsza_rk(y)




