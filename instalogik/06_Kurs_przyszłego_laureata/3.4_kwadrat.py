a = 3
b = 4
print("")
print("opcja 1:")
for y in [1, 2, 3, 4]:
    print("***");

print("")
print("opcja 2:")
while b > 0:
    b = b - 1
    print("***")

print("\nopcja 3:")
while a > 0:
    print("*", end="")
    a = a - 1

print("\n\nopcja 4:")
a = 4
b = 3
print(f"a={a} b={b}")
while b > 0:
    b = b - 1
    c = a
    while c > 0:
        print('x', end="")
        c = c - 1
    print('')
