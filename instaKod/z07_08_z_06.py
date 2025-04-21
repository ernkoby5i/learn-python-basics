a = int(input())
b = int(input())

n = b
i = 0
while n > a:
    if n % 2 == 0:
        if i!=0:
            print(" ", end='')
        print(n, end='')
        i = i + 1
    n = n - 1
