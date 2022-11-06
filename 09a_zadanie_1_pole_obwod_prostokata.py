# Zadanie 1
# Step 1: napisz funkcje obwod_prostokata(a,b)
# Step 2: napisz funkcje pole_prostokata(a,b)

import math


def obwod_prostokonta(a, b):
    print(f"obliczam obwód a={a} b={b}")
    obwod = a * 2 + b * 2
    return obwod


def pole_prostokonta(a, b):
    print("obliczam pole a=" + str(a) + " b=" + str(b))
    pole = a * b
    return pole


def obwod_trojkta(a, b, c):
    print(f"obliczam obwód a={a} b={b} c={c}")
    obwod = a + b + c
    return obwod

# Wzor Herona
def pole_trojkata(a, b, c):
    print("obliczam pole a=" + str(a) + " b=" + str(b) + " c=" + str(c))
    p = 1 / 2 * (a + b + c)
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return pole


print("Obwod prostokata : " + str(obwod_prostokonta(5, 3)))
print("pole prostokata : " + str(pole_prostokonta(5, 3)))
print("Obwod trójkata : " + str(obwod_trojkta(5, 3, 4)))
print("pole trójkonta : " + str(pole_trojkata(4, 5, 7)))
