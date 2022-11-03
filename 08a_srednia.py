oceny_ernest = [['polski',5],
         ['angielski',2],
         ['wf',6],
         ['biol',5],
         ['Matma',4]]

oceny_maja = [['polski',5],
         ['angielski',5],
         ['wf',5],
         ['biol',5],
         ['chemia',5],
         ['Matma',5]]

suma_ocen = 0
ilosc_przedmiotow = 0

for x in oceny_maja:
    przedmiot = x[0]
    ocena = x[1]
    print(przedmiot,ocena )
    suma_ocen = suma_ocen + x[1]
    ilosc_przedmiotow = ilosc_przedmiotow + 1


print('podsumowanie:')
print('suma_ocen = ', suma_ocen)
print('ilosc_przedmiotow = ', ilosc_przedmiotow)
print('srednia = ',suma_ocen / ilosc_przedmiotow )
