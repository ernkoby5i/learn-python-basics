a = int(input())
b = int(input())
if a>b:
    c = a
    a = b
    b = c
m = a
while m < b:
    if (m%3!=0):
        print(m)
    m = m + 1