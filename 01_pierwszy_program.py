a=2
b=3
c=a+b
print(a, b, c)

s1="ernesto"
s2="lenozałrus"
ss=s1+" i "+s2
print(ss)
print(ss[2])

# Listy
dzieci = ["Maja", "ernest"]
print (dzieci)
dzieci.append("lena")
print (dzieci)
print(dzieci[1])

#tuples
przedmiot=("Matematyka",5)
print(przedmiot)
print(przedmiot[1])

#SLOWNIKI
slownik = {
    "Matematyka":5,
    "polski":4
}
print(slownik["Matematyka"])

portfel = 10
bulka_cena = 3
#ilosc = int(input("podaj ilosc bulek:"))
ilosc = 3
if (ilosc * bulka_cena <= portfel):
    print("wystarczy pieniedzy")
else:
    print("NIE wystarczy pieniedzy")

twoja_srednia = 4.8

if (twoja_srednia >= 4.75):
    print(f"twoja srednia {twoja_srednia}")
    print("czerwony pasek")
else:
    print(f"twoja srednia {twoja_srednia}")
    print("NIE bedzie paska")

