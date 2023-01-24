## Exerciții obligatorii - grad de dificultate: Ușor spre Mediu: ##

'''
1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
'''

# Variabila = locatie de memorie in care se stochează valori.

'''
2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :
- string
- int
- float
- bool
Observație: Valorile vor fi alese de tine după preferințe.
'''

name = "Gabi"
age = 37
height_m = 1.70
isWoman = True

'''
3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
'''

print(type(name))
print(type(age))
print(type(height_m))
print(type(isWoman))

'''
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
'''

height_m = round(height_m)
print(height_m)
print(type(height_m))

'''
5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.

Rezolvă nepotrivirile de tip prin ce modalitate dorești.
'''

print(f'My name is {name}.')
print(f'I am {age} years old.')
print(f'I am aproximately {height_m} m tall.')
print(f'It is {isWoman} that I am a woman.')

'''
6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
'''

lastName = input('Your last name is: ')
firstName = input('Your first name is: ')
x = len(lastName) + len(firstName)
print(f'Numele complet are ' + str(x) + ' caractere')

'''
7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
'''

ab = input('Lungime:')
bc = input('latime:')
a = int(ab)*int(bc)
print('Aria dreptunghiului este ' + str(a))

'''
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':

- afișează de câte ori apare cuvântul 'the';
'''

message = 'Coral is either the stupidest animal or the smartest rock'
occurrence = ' the '
x = message.count(occurrence)
print(x)

'''
9. Același string.
● Afișează de câte ori apare cuvântul 'the';
● Printează rezultatul.
'''

print(f'Cuvantul "the" apare de ' + str(x) + ' ori')

'''
10. Același string.
● Folosiți un assert ca să verificați dacă acest string conține doar numere.
'''

assert message.isnumeric(), 'The message does not contain only numbers'
print('The message contains only numbers')


## Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai nevoie de Google). ##

'''
1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
'''

x = input('Enter an odd word: ')
print(f'The middle letter is: ' + x[len(x)//2])

'''
2. Folosind assert, verifică dacă un string este palindrom.
'''

p = input('Enter a word: ')
assert p == p[::-1], 'The word is not a palindrome'  # parcurgere inversa
print('The word is a palindrome')

'''
3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
'''

x, y = input('Enter 2 values: ').split()
print(x)
print(y)

text = input('Scrie un string: ')
x, y = text.split(' ')
print(f'Primul cuvant este: {x}')
print(f'Ultimul cuvant este: {y}')

'''
4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
'''

txt = input('Enter text:')
x = txt[0]
y = txt[-1]
print(x + txt[1:-1].replace(x, x.upper()) + y)

'''
5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****
'''

user = input('Enter User: ')
password = input('Enter Password: ')
char_count = len(password)
star = '*' * char_count
print(f'Parola pt user {user} este {star} si are {char_count} caractere')

