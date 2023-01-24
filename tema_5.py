## Exerciții obligatorii - grad de dificultate: Usor spre Mediu ##

'''
1.Funcție care să calculeze și să returneze suma a două numere
'''
x = int(input('Introdu primul numar: '))
y = int(input('Introdu al doilea numar: '))


def suma_numere(x, y):
    suma = x + y
    return f'Suma celor doau numere este: {suma}'


print(suma_numere(x, y))
'''
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
'''


def even(n):
    return n % 2 == 0


x = int(input('Introdu un numar: '))
print(even(x))

'''
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
'''


def sum_name(surname, first_name, middle_name):
    suma = len(surname + first_name + middle_name)
    return suma


print(f'Numarul total de caractere din numele Sandu Gabriela Sorina este: ', sum_name('Sandu', 'Gabriela', 'Sorina'))

'''
4. Funcție care returnează aria dreptunghiului
'''


def aria_drep(lungime, latime):
    aria = lungime * latime
    return aria


a = int(input('Introdu Lungimea dreptunghiului: '))
b = int(input('Introdu latimea dreptunghiului: '))
print('Aria dreptunghiului este: ', aria_drep(a, b))

'''
5. Funcție care returnează aria cercului
'''


def aria_cerc(raza):
    pi = 3.14159265
    aria = round(pi * raza * raza, 2)
    return aria


x = int(input('Introdu raza cercului: '))
print(f'Aria cercului cu o raza {x} este: ~', aria_cerc(x))


'''
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și Talse dacă nu găsește.
'''


def char_in_string(string, x):
    if x in string:
        return True
    else:
        return False


a = input('Enter string: ')
b = input('Enter char to find: ')
print(char_in_string(a, b))


'''
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
'''

string = input('Enter a string: ')


def low_upp(n):
    uppercase = 0
    lowercase = 0
    for char in n:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        else:
            pass
    print('Nr de caractere upper case este', uppercase)
    print('Nr de caractere lower case este', lowercase)


low_upp(string)

'''
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
'''

myList = [-12, -11, -10, 23, 0, 15, -88, 11]


def numere_pozitive(numere):
    positive_list = []
    for i in numere:
        if i > 0:
            positive_list.append(i)
    return positive_list


print(numere_pozitive(myList))

'''
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
'''

i = int(input('Enter First number: '))
j = int(input('Enter Second number: '))


def compare_num(x, y):
    if x == y:
        print(f'The numbers are equal')
    elif x > y:
        print(f'The first number {x} is greater than the second number {y}')
    else:
        print(f'The second number {y} is greater than the first number {x}')


compare_num(i, j)

'''
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
'''
set_numbers = {12, 23, 34, 45, 56, 67}


def add_number(set_num, number):
    if number in set_numbers:
        print(f'Nu am adaugat numarul nou {number} in set, exista deja')
        return False
    else:
        set_num.add(number)
        print(f'Am adaugat numarul {number} in set')
        return True


print(add_number(set_numbers, 67))
print(add_number(set_numbers, 78))
print(set_numbers)


## Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.##

'''
1. Funcție care primește o lună din an și returnează câte zile are acea luna
'''


def calendar(month):
    year = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
    }
    if month in year:
        return year.get(month)


x = input('Enter the name of the month: ').capitalize()
print(calendar(x))


'''
2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a)

● print("Diferenta: ", b)
● print("Inmultirea: ", c)
● print("Impartirea: ", d)
'''


def calculator(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d


a, b, c, d = calculator(15, 5)

print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

'''
3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''

list1 = [1, 3, 1, 5, 9, 7, 7, 5, 5]


def count(lista):
    dct = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }
    for i in dct.keys():
        for j in lista:
            if i == j:
                dct[i] = dct[i] + 1
    return dct


print(count(list1))


'''
4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
'''


def maxim(x, y, z):
    if x == y == z:
        return ('The numbers are equal')
    elif x >= y and x >= z:
        return (f'{x} is the highest number')
    elif y >= x and y >= z:
        return (f'{y} is the highest number')
    else:
        return (f'{z} is the highest number')


a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

print(maxim(a, b, c))


'''
5. Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
'''


def sum_num(a):
    suma = 0
    for i in range(0, a + 1):
        suma = suma + i
    return suma


x = int(input('Enter a number between 0 and 10: '))
print(f'Suma tuturor numerelor de la 0 la {x} este:', sum_num(x))


## Exerciții Opționale - Bonus ##

'''
1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune

Exemplu:
list1 = [1, 1, 2, 3]

list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
'''

list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]


def common_nr(l1, l2):
    a1 = set(l1)
    a2 = set(l2)
    return a1.intersection(a2)


print(f'Numerele comune intre {list1} si {list2} sunt:', common_nr(list1, list2))


'''
2.. Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.
'''


def discount(price, sale):
    if sale > 100 or sale < 0:
        return 'Invalid discount'
    discounted_price = price - (sale / 100) * price
    return discounted_price


p = int(input('Enter the price: '))
d = int(input('Enter the discount percentage: '))
print(discount(p, d))


'''
3. Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)
'''

from datetime import datetime


def data_ora():
    date_time = datetime.now()
    dt_string = date_time.strftime("%d/%m/%Y %H:%M:%S")
    print("Date and Time in RO: ", dt_string)


data_ora()


'''
4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)
'''

from datetime import date


def countdown_date(year):
    b_day = date(year=year, month=2, day=28)
    days_til_b_day = (b_day - date.today()).days
    return days_til_b_day


print(countdown_date(2023))
