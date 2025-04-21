n = int(input())

x = int(input())

min = x
max = x

m = n - 1
while m>0:
    n = int(input())
    if n<min:
        min = n
    if n>max:
        max = n
    m = m-1
print(min)
print(max)