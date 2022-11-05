def funkcja_test():
    print("funkcja....")

    funkcja_test()

def dodaj(x):
    print(x + 1)

zmienna = dodaj(2)
print(zmienna)

def dodaj(x, y = 1, z = 0):
    return x + y + z
    print("czy ja istnieje")

print(dodaj(2, 3))
print(dodaj(2))
wynik = dodaj(2, 3, 5)
print(wynik)


