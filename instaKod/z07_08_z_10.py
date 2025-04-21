n = int(input())

x = int(input())


max = x
i = 1

m = n - 1
while m>0:
    n = int(input())
    if max == n:
        i = i+1
    if n>max:
        max = n

        i = 1
    m = m-1

print(i)