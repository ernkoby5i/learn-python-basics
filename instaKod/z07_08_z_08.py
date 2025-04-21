n=int(input())
m = n - 1
x = int(input())
min = x
while m>0:
    n = int(input())
    if n<min:
        min = n
    m = m-1
print(min)