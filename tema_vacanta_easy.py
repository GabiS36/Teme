## TEMA VACANTA – Easy Mode ##
'''
Ex1.
Creeaza 3 liste care sa contina animale:
Mamifere
Reptile
Pasari
Sorteaza fiecare lista alphabetic
Creeaza alte 3 liste in care sa salvezi aceleasi elemente din primele 3 liste, dar cuvintele sa fie pe dos. Exemplu insect_list = [“greiere”, “musca”] 🡪 insect_list_r = [“ereierg”, “acsum”]
Numara caracterele din fiecare element string din fiecare lista si afiseaza lista cu cele mai multe caractere.
Inlocuieste fiecare al doilea element din fiecare lista cu “I am an intruder”
Sa se amestece toate elementele random din prima lista. Poti folosi .shuffle()
Sa se parcurga lista si daca se gaseste elemental “I am an intruder”, sa se returneze pozitia lui, sa se stearga din lista si sa se returneze mesajul “The intruder was kicked out”
'''

# Ex 1 - 1

mamifere = ["Capra", "Arici", "Cal", "Bursuc", "Babuin"]
reptile = ["Crocodil", "Soparla", "Lipitoare", "Varan", "Aligator"]
pasari = ["Fazan", "Corb", "Barza", "Cocos", "Bufnita"]

# Ex 1 - 2

mamifere.sort()
reptile.sort()
pasari.sort()


# Ex 1 - 3
def revers_list(lista):
    return [i[::-1] for i in lista]


mamifere_r = revers_list(mamifere)
reptile_r = revers_list(reptile)
pasari_r = revers_list(pasari)

print(mamifere_r)
print(reptile_r)
print(pasari_r)


# Ex 1 - 4
def longest(lista):
    long = 0
    for i in lista:
        long += len(i)
    return long


x = longest(mamifere)
y = longest(reptile)
z = longest(pasari)

if x > y and x > z:
    print(mamifere, f'este lista cu cele mai multe caractere:\n{x} caractere')
elif y > z:
    print(reptile, f'este lista cu cele mai multe caractere:\n{y} caractere')
else:
    print(pasari, f'este lista cu cele mai multe caractere:\n{z} caractere')


# Ex 1 - 5
def repl_second(list):
    list[1] = 'I am an intruder'
    return list


print(repl_second(mamifere))
print(repl_second(reptile))
print(repl_second(pasari))


# Ex 1 - 6
import random

random.shuffle(mamifere)
print(mamifere)


# Ex 1 - 7

index = mamifere.index('I am an intruder')
del mamifere[index]
print('The intruder was kicked out', mamifere)


'''
Ex2.
Creeaza clasa animal cu 4 atribute si 2 metode
Creeaza alte 3 clase care sa mosteneasca clasa animal si adauga inca o metoda
'''
class Animal:
    def __init__(self, species, name, age, status):
        self.species = species
        self.name = name
        self.age = age
        self.status = status

    def get_details(self):
        print(f'Details: {self.species}, {self.name}, {self.age}, {self.status}')

    def call_to_action(self):
        if self.status == 'Available':
            print(f'Adopt the {self.species} named {self.name}!')
        else:
            print(f'{self.name} is not available for adoption')


class Dog(Animal):
    def __init__(self, species, name, age, status, breed):
        super().__init__(species, name, age, status)
        self.breed = breed

    def adopt(self):
        if self.status == 'Available':
            print(f'Congrats for your new friend, the {self.breed} {self.species} {self.name}')
            self.status = 'Adopted'
        else:
            print(f'Keep looking')


class Cat(Animal):
    def __init__(self, species, name, age, status, breed):
        super().__init__(species, name, age, status)
        self.breed = breed

    def adopt(self):
        if self.status == 'Available':
            print(f'Congrats for your new friend, the {self.breed} {self.species} {self.name}')
            self.status = 'Adopted'
        else:
            print(f'Keep looking')


class Pig(Animal):
    def __init__(self, species, name, age, status, breed):
        super().__init__(species, name, age, status)
        self.breed = breed

    def adopt(self):
        if self.status == 'Available':
            print(f'Congrats for your new friend, the {self.breed} {self.species} {self.name}')
            self.status = 'Adopted'
        else:
            print(f'Keep looking')


dog1 = Dog('Dog', 'Azorel', '0.3 years old', 'Available', 'Akita Inu')
cat1 = Cat('Cat', 'Kitty', '2 years old', 'Available', 'Sphynx')
pig1 = Pig('Pig', 'July', '0.4 years old', 'Adopted', 'Guinea Hog')

dog1.get_details()
dog1.call_to_action()
dog1.adopt()


cat1.get_details()
cat1.call_to_action()
cat1.adopt()

pig1.get_details()
pig1.call_to_action()
pig1.adopt()

'''
Ex3.
Sa se introduca un cuvant de la tastatura si sa se afiseze ce lungime are, cate consoane, cate vocale are si daca are vreun numar in compozitie.
'''


def details(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    length = len(word)
    c_ctr = 0
    v_ctr = 0
    for i in word:
        if i in vowels:
            v_ctr += 1
        else:
            c_ctr += 1
    print(f'The length of the word {word} is: {length} characters')
    print(f'The word {word} has {v_ctr} vowels')
    print(f'The word {word} has {c_ctr} consonants')


def containsNumber(word):
    for char in word:
        if char.isdigit():
            print(f'The word {word} contains numbers')
            break
    else:
        print(f'The word {word} does not contain any numbers')


string = input('Enter a word: ').lower()
details(string)
containsNumber(string)


'''
Ex4.
1.   Sa se creeze un dictionar cu 5 carti care sa contina numele cartii, autorul, nr_pag, mesaj (daca este available sau nu)
2.   Sa se creeze o functie care sa ii permita bibliotecarului sa poate adauga carti noi in biblioteca (dictionar).
3.   Sa se creeze o functie care sa ii permita bibliotecarului sa poata sterge carti din biblioteca
4.   Sa se creeze o functie care sa ii permita bibliotecarului sa introduca un nume de carte si sa verifice daca este available sau nu
'''


def list_books(library):
    for book in library:
        print()
        print('Title: ', book)
        print('Author: ', library[book]['Autor'])
        print('No of pages: ', library[book]['nr_pag'])


def add_new_book(library):
    title = input('Title to add: ').title()
    if title in library:
        print(title + ' already exists in the library')
        return

    author = input('Author name: ').title()
    nr_pag = input('Enter number of pages: ')
    mesaj = input('Enter status - Available/Not Available: ').title()

    book = {'Autor': author, 'nr_pag': nr_pag, 'mesaj': mesaj}

    library[title] = book
    print(title + ' has been added to the Library')


def delete_book(library):
    title = input("Title to delete: ").title()
    if title in library:
        del library[title]
        print(title + ' was removed from library.')
    else:
        print(title + ' does not exist in the library.')


def show_status(library):
    title = input('Title to check status: ').title()
    if title in library:
        book = library[title]
        print('The book is: ' + book['mesaj'])
    else:
        print('Sorry, ' + title + ' does not exist in the library')


def display_menu():
    print('COMMAND MENU')
    print('list - List all books in the library')
    print('add - Add new book')
    print('del - Delete book')
    print('status - Available/Not Available')


def main():
    display_menu()
    library = {
        'Carte1':
            {'Autor': 'Autor1', 'nr_pag': 220, 'mesaj': 'Available'},
        'Carte2':
            {'Autor': 'Autor2', 'nr_pag': 220, 'mesaj': 'Available'},
        'Carte3':
            {'Autor': 'Autor3', 'nr_pag': 220, 'mesaj': 'Available'},
        'Carte4':
            {'Autor': 'Autor4', 'nr_pag': 220, 'mesaj': 'Available'},
        'Carte5':
            {'Autor': 'Autor5', 'nr_pag': 220, 'mesaj': 'Not Available'}
    }
    while True:
        print()
        command = input('Command: ').lower()
        if command == 'list':
            list_books(library)
        elif command == 'add':
            add_new_book(library)
        elif command == 'del':
            delete_book(library)
        elif command == 'status':
            show_status(library)
        else:
            print('Unknown command. Please try again')
            display_menu()


main()

'''
Ex5. – Medium
Un user poate sa creeze o rezervare la restaurant care sa contina nume, data, ora, numar persoane, numar mese.
Numarul de mese se va calcula automat in functie de numarul de persone introdus de utilizator. O masa stim ca poate sa aiba 6 locuri.
Cand veti rula programul va aparea prima data un mesaj de genul:
==== “Welcome to our restaurant restaurant_name” ====.
Puteti alege voi numele restaurantului si mesajul de welcome.
Clientul va fi intrebat daca vrea sa faca o rezervare
Daca raspunde nu, atunci va primi mesajul, “Maybe next time! Have a nice day!”
Daca raspunde da, atunci va fi intrebat numele, data, ora si numarul de persoane.
Dupa ce utilizatorul a introdus datele va fi anuntat ca rezervarea a fost creata:
Reservation was created on the name X, on date Y, at Z hour for N persons.
Sa se foloseasca functii.
Sa se creeze si o functie care apelata va returna lista de rezervari.
'''


def list(restaurant):
    for rezervatio in restaurant:
        print()
        print('Rezervation:')
        print('Name: ', restaurant[rezervatio]['name'])
        print('Date: ', restaurant[rezervatio]['date'])
        print('Time: ', restaurant[rezervatio]['time'])
        print('Number of persons: ', restaurant[rezervatio]['n_pers'])
        print('Number of tables: ', restaurant[rezervatio]['n_table'])


def add_reservation(restaurant):
    response = input("Would you like to make a rezervation? (y/n)").lower()

    if response == 'y':
        rezervation = input('Rezervation name: ').title()
    else:
        print('“Maybe next time! Have a nice day!”')
        return

    date = input('Rezervation date: ')
    time = input('Rezervation time: ')
    n_pers = int(input("Enter the number of persons: "))
    n_table = 0
    for i in range(0, n_pers, 6):
        n_table += 1
    print('Number of tables: ', n_table)

    rez = {'name': rezervation,
           'date': date,
           'time': time,
           'n_pers': n_pers,
           'n_table': n_table}

    restaurant[rezervation] = rez
    print(f'Reservation was created on the name {rezervation}, on date {date}, at {time} hour for {n_pers} persons')


def welcome():
    print('==== “Welcome to our restaurant Arrakis” ====')


def main():
    welcome()
    restaurant = {
        'Rezervare1':
            {'name': 'Nume 1', 'date': 12.02, 'time': '18:00', 'n_pers': 6, 'n_table': 1},
        'Rezervare2':
            {'name': 'Nume 2', 'date': 12.02, 'time': '18:00', 'n_pers': 12, 'n_table': 2},
        'Rezervare3':
            {'name': 'Nume 3', 'date': 12.02, 'time': '18:00', 'n_pers': 4, 'n_table': 1},
    }
    while True:
        print()
        command = input('COMMANDS:\nlist - List all rezervations in the restaurant\nadd - Add new rezervation\n'
                        'Command: ').lower()
        if command == 'list':
            list(restaurant)
        elif command == 'add':
            add_reservation(restaurant)
        else:
            print('Unknown command. Please try again')


main()
