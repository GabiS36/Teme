import random

# Exerciții obligatorii - grad de dificultate: Usor spre Mediu ##

'''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']

# for each
for masina in masini:
    print(f'Masina mea preferata este {masina}')

# while
length = len(masini)
i = 0

while i < length:
    print('Masina mea preferata este', masini[i])
    i += 1

# for
for i in range(length):
    print('Masina mea preferata este', masini[i])


'''
2. Aceeași listă:
Folosește un for else
În for

- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
for masina in range(1, len(masini[:-1])):
    masini[masina] = masini[masina].upper()
else:
    print(masini)

'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
'''

masini = ['Audi', 'Volvo', 'Bmw', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
masina_a = input('Ce masina doresti? ').title()

while masina_a in masini:
    print('am gasit masina dvs', masina_a)
    break
else:
    print('nu am gasit masina', masina_a, 'mai cautam')


'''
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
for i in masini:
    if i == 'Trabant' or i == 'Lăstun':
        continue
    print('S-ar putea sa va placa masina: ', i)

'''
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).

● Printează Modele vechi: x.
● Modele noi: x.
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for i in masini:
    if i == 'Trabant' or i == 'Lăstun':
        masini_vechi.append(i)
        index1 = masini.index(i)
        masini[index1] = 'Tesla'
print(masini_vechi)
print(masini)

'''
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
'''
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

x = pret_masini.items()
buget = int(input('Enter buget: '))

for car, price in x:
    if price <= buget:
        print(f'Pentru un buget de sub', buget, 'pueteti alege masina', car, 'la pretul de', price)

'''
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
count = 0

for numar in numere:
    if numar == 3:
        count += 1
print('numarul 3 apare de', count, 'ori')

'''
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0

for num in numere:
    suma += num
print('suma numerelor din lista este: ', suma)

'''
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
largest = None

for num in numere:
    if largest is None or largest < num:
        largest = num
print('numarul cel mai mare din lista este: ', largest)

'''
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

# Solutia 1:
numere_a = [-abs(number) for number in numere]
print(numere_a)

# Solutia 2:
num = []
for number in numere:
    num.append(-abs(number))
print('Lista a devenit', num)


# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.##

'''
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
'''

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for num in alte_numere:
    if num % 2 == 0:
        numere_pare.append(num)
    else:
        numere_impare.append(num)
    if num > 0:
        numere_pozitive.append(num)
    else:
        numere_negative.append(num)

print('Numerele pare sunt: ', numere_pare)
print('Numerele impare sunt: ', numere_impare)
print('Numerele pozitive sunt: ', numere_pozitive)
print('Numerele negative sunt: ', numere_negative)

'''
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
'''

numere1 = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(numere1)):
    for j in range(i + 1, len(numere1)):
        if numere1[i] > numere1[j]:
            numere1[i], numere1[j] = numere1[j], numere1[i]
print(numere1)

'''
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr

Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
'''

numar_secret = random.randint(1, 30)
numar_ghicit = None

while numar_ghicit is None:
    nr = int(input('Introdu un numar: '))
    if nr > numar_secret:
        print('Numarul secret este mai mic')
    elif nr < numar_secret:
        print('Numarul secret este mai mare')
    else:
        print('Felicitari, ai gasit numarul!')
        break

'''
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
'''

rows = int(input('Enter a number between 1 and 7: '))

for i in range(rows+1):
    for j in range(i):
        print(i, end='')
    print('')

'''
5.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
'''

tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este {tastatura_telefon[i][j]}')
