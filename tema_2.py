## Exerciții obligatorii - grad de dificultate: Ușor spre Mediu: ##

'''
1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
'''
# If else - este un flow control tool care controleaza flow-ul programului.
# Se evalueaza o conditie declarata, iar programul va continua diferit in functie
# de aceasta. Daca conditia e intalnita, e evaluata ca si Adevarata. Altfel, declaratia va fi evaluata ca si Falsa.
'''
2. Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural
daca este numar intreg mai mare ca 0)
'''

x = int(input('Enter a number: '))
if x > 0:
    print(f'{x} is a natural nr')
else:
    print(f'{x} is not a natural number')

'''
3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
'''
# Solutia 1:

x = int(input('Enter any number: '))
if x < 0:
    print(f'{x} is negative')
elif x == 0:
    print(f'{x} is neutral')
else:
    print(f'{x} is positive')

# Solutia 2:

x = input('Enter any number: ')
if x.isdigit() and int(x) < 0 or float(x) < 0:
    print(f'{x} is negative')
elif x.isdigit() and int(x) > 0 or float(x) > 0:
    print(f'{x} is positive')
else:
    print(f'{x} is neutral')


'''
4. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).
'''

x = int(input('Enter a number'))
if (x > -2) and (x < 13):
    print(f'{x} is between -2 and 13')
else:
    print(f'{x} is not between -2 and 13')

'''
5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
abs
'''
### Testeaza
print('Enter two numbers: ')
x = int(input('x: '))
y = int(input('y: '))
if 5 > x - y:
    print(f'Diferenta intre {x} si {y} este mai mica de 5')
else:
    print(f'Diferenta intre {x} si {y} nu este mai mica de 5')

'''
6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
'''

x = int(input('Enter a number: '))
if not((x > 5) and (x < 27)):
    print(f'{x} is not between 5 and 27')
else:
    print(f'{x} is between 5 and 27')

'''
7. Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
daca nu, afiseaza care din ele este mai mare
'''
### Testeaza

x = int(input('Enter First number: '))
y = int(input('Enter Second number: '))

if x == y:
    print(f'{x} and {y} are equal')
elif x > y:
    print('The largest number of the 2 is:', x)
else:
    print('The largest number of the 2 is:', y)


'''
8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
oarecare (nicio latura nu e egala).
'''

print("Input the lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

##### verify the validity of a triangle: suma lungimii a doua laturi este mai mare sau egala cu a cea de-a treia (si niciuna dintre laturi nu e 0 sau mai mica de 0).

if not (x <= y + z and y <= x + z and z <= x + y) or x <= 0 or y <= 0 or z <= 0:
    print('It is not a triangle')

##### verify if a valid triangle is: echilateral, isoscel sau oarecare:

elif x == y == z:
    print('The triangle is Equilateral')
elif x == y or y == z or x == z:
    print('The Triangle is Isosceles')
else:
    print('The Triangle is "Oarecare"')


'''
9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
'''


# Solutia 1:
x = input('Enter any letter: ')
if x.lower() in ('a', 'e', 'i', 'o', 'u'):
    print("The letter is a Vowel")
else:
    print("The letter is not a Vowel")


# Solutia 2:
x = input("Enter any letter: ")
if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
    print(f'{x} is a Vowel.')
else:
    print(f'{x} is not a Vowel.')



'''
10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum
urmeaza:
a. Peste 9 => A
b. Peste 8 => B
c. Peste 7 => C
d. Peste 6 => D
e. Peste 4 => E
f. 4 sau sub => F
'''

# Solutia 1:
x = int(input('Enter your romanian grade: '))
if x == 10:
    print(f'{x} => A')
elif x == 9:
    print(f'{x} => B')
elif x == 8:
    print(f'{x} => C')
elif x == 7:
    print(f'{x} => D')
elif x == 5 or x == 6:
    print(f'{x} => E')
elif 4 >= x >= 1:
    print(f'{x} => F')
else:
    print(f'{x} is not a valid grade')


# Solutia 2:
x = float(input('Enter your grade: '))
if x > 9 or x == 10:
    print(f'{x} => A')
elif x > 8 or x == 9:
    print(f'{x} => B')
elif x > 7 or x == 8:
    print(f'{x} => C')
elif x > 6 or x == 7:
    print(f'{x} => D')
elif x > 4 or x == 6:
    print(f'{x} => E')
elif x <= 4 and not(x < 1):
    print(f'{x} => F')
else:
    print(f'{x} is not a valid grade')


## Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai nevoie de Google). ##

'''
1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''

x = int(input('Enter at least 4 digits: '))
y = len(str(x))
if y >= 4:
    print(f'{x} are minim 4 cifre')
else:
    print(f'{x} nu are minim 4 cifre')

'''
2. Verifica daca x are exact 6 cifre
'''

x = input('Enter exactly 6 digits number: ')
y = len(x)
if y == 6 and x.isdigit():
    print(f'{x} has exactly 6 digits')
elif not(x.isdigit()):
    print(f'{x} Is not a number')
else:
    print(f'{x} does not have exactly 6 digits')

'''
3. Verifica daca x este numar par sau impar
'''

x = int(input('Enter a number: '))
if x % 2 != 0:
    print(f'{x} is  odd')
else:
    print(f'{x} is even')

'''
4. Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre
ele
'''

x = int(input('Enter First number: '))
y = int(input('Enter Second number: '))
z = int(input('Enter Third number: '))
if x == y == z:
    print('the numbers are equal')
elif (x > y) and (x > z):
    print(f'{x} is largest')
elif (y > x) and (y > z):
    print(f'{y} is largest')
else:
    print(f'{z} is largest')


'''
5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca
triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de
180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat
lungimea celei de-a treia laturi)
'''
x = int(input('Enter the first triangle angle value: '))
y = int(input('Enter the second triangle angle value: '))
z = int(input('Enter the third triangle angle value: '))
# Check if the angles sum is 180
if (x + y + z == 180) and x != 0 and y != 0 and z != 0:
    print('The Triangle is valid')
else:
    print('The triangle is invalid')

'''
6. Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de
la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă
ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the
smarte'
'''
a = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('How many chars you want to remove? '))
print(f'{a[: - x]}')

'''
7. Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format
din primele 5 caractere + ultimele 5
'''
a = 'Coral is either the stupidest animal or the smartest rock'
b = a[:5] + a[-5:]
print(b)

'''
8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
(hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
animal or the smartest '
'''
# Solutia 1:

a = 'Coral is either the stupidest animal or the smartest rock'
c = a.index('rock')
sliced_a = slice(c)
print(a[sliced_a])

# Testeaza
# Solutia 2:
a = 'Coral is either the stupidest animal or the smartest rock'
c = a.index('rock')
print(a[:c])
'''
9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se
va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o
functie pentru a face string-ul case insensitive)
'''

x = input('Enter string: ')
first_char = x[0].lower()
last_char = x[-1].lower()
assert first_char == last_char, 'Primul si ultimul caracter nu sunt la fel'
print('Primul si ultimul caracter sunt la fel')

'''
10.  Avand stringul '0123456789'
● Afișați doar numerele pare
● Afișați doar numerele impare
(hint: folositi slicing, controlați din pas)
'''

x = '0123456789'
print(f'The even numbers are:', x[::2])
print(f'The odd numbers are:', x[1::2])


## Exerciții Bonus ##

'''
1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
inputuri urmatoarele informatii:
a. Varsta
b. Insotit de mama
c. Insotit de tata
d. Pasaport
e. Act permisiune mama
f. Act permisiune tata
Conditii de imbarcare:
1. Daca pers are varsta peste 18 ani si are pasaport
2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
si are permisiune in scris de la celalat parinte

Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate
variantele care crezi ca ar trebui testate. Genereaza scenarii de testare cu expected results si
apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.
Exemple:
1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
'''

## Testeaza
varsta = int(input("Va rugam sa introduceti varsta pasagerului "))
pasaport_valid = input("E pasaportul valid? Da/Nu ")
if varsta>=18 and pasaport_valid == "Da":
    print("Va puteti imbarca")
elif varsta<18 and pasaport_valid == "Da":
    ambii_parinti = input("E copilul insotit de ambii parinti? ")
    if ambii_parinti == "Da":
        print("Va puteti imbarca")
    else:
        permisiune = input("Permisiune parinte lipsa: ")
        if permisiune == "Da":
            print("Va puteti imbarca")
        else:
            print("Nu va puteti imbarca")
else:
    print("Nu va puteti imbarca")

'''
2. Joc de noroc
- Cauta pe net si vezi cum se genereaza un numar random
- Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
Numarul salvat va fi generat random cu metoda gasita in online
- Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
- Verifica si afiseaza daca utilizatorul a ghicit numarul
- Vor exista 3 optiuni care vor trebui tratate:
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari? Ai ales x si zarul a fost y
'''

### Testeaza:
import random

dice_roll = random.randint(1, 6)
print('Guess the number')
guess = input('Enter a number between 1 and 6: ')
if not(str(guess).isdigit()):
    print(f'{guess} is not a number')
elif dice_roll < int(guess) and int(guess) in range(1, 7):
    print(f'You lose. Your number is higher. You chose {guess} but the roll was {dice_roll}')
elif dice_roll > int(guess) and int(guess) in range(1, 7):
    print(f' You lose.Your number is lower. You chose {guess} but the roll  was {dice_roll}')
elif dice_roll == int(guess) and int(guess) in range(1, 7):
    print(f'You guessed. Congratulations! You chose {guess} and the roll was {dice_roll}')
else:
    print(f'{int(guess)} is not between 1 and 6')


