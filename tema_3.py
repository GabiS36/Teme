## Exerciții obligatorii - grad de dificultate: Ușor spre Mediu:##

'''
1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
a. Afiseaz-o
b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza
varianta actuala (inversata)
c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face
asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
varianta inițială
Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa
suprascrii lista sau sa o salvezi intr-o listă nouă. Metoda gasita de tine face
suprascrierea automat și permanentizeaza aceste modificări. Ambele variante își
găsesc utilitatea în funcție de ce ne dorim in acel moment.
'''

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# a.
print(note_muzicale)
# b.
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
# c.
note_muzicale.reverse()
print(note_muzicale)

'''
2. Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.
'''
print(note_muzicale.count('do'))
'''
3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.
'''
ls1 = [3, 1, 0, 2]
ls2 = [6, 5, 4]
ls3 = ls1 + ls2
print(ls3)
ls1.extend(ls2)
print(ls1)

'''
4. Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista
folosind o functie si apoi afiseaza din nou lista
'''

ls1.sort()
print(ls1)
elem = ls1[0]
ls1.remove(elem)
print(ls1)

'''
5. Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura
urmatoarele:
- Lista este goala (IF)
- Lista nu este goala (ELSE)
'''
if len(ls1) == 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

'''
6. Foloseste o functie care sa goleasca lista de la exercitiul 3
'''

ls1.clear()

'''
7. Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se
afiseze ca lista e goala
'''

if len(ls1) == 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

'''
8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa
afisezi Elevii (cheile)
'''

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())

'''
9. Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
Ex: ‘Ana a luat nota {x}’.
Doar nota o vei lua folosindu-te de cheie
'''

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print('Ana a luat nota', dict1['Ana'])
print('Gigel a luat nota', dict1['Gigel'])
print('Dorel a luat nota', dict1['Dorel'])

'''
10. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
- Modifica nota lui Dorel in 6
- Printeaza nota lui dupa modificare
'''
# Solutia 1:

dict1.update({"Dorel": 6})
print(dict1)
print('Dorel a luat nota', dict1['Dorel'], 'dupa contestatie')

# Testeaza
# Solutia 2:

dict1["Dorel"] = 6
print('Dorel a luat nota', dict1['Dorel'], 'dupa contestatie')

'''
11. Imagineaza-ti ca Gigel se transfera din clasa.
- Cauta o functie care sa il stearga
Vine un coleg nou.
- Adaugati-l in lista pe Ionica, cu nota 9
- Printati dictionarul cu noii elevi
'''

dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)

'''
12. Ai urmatoarele seturi:
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
- Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
- Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.
'''

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

'''
13. Foloseste un if si verifica daca:
- Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
regasesc intre elementele din setul zile_sapt)
- Weekend nu este un subset al zilelor din sapt
Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui
punct de mai sus va fi un boolean
'''

if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săpt.')
else:
    print('Weekend nu este un subset al zilelor din săpt.')

'''
14. Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu
sunt in weekend si invers)
'''

print(zile_sapt.difference(weekend))

'''
15. Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in
ambele seturi). Hint: Va puteti folosi de o functie
'''

print(zile_sapt.intersection(weekend))

## Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai nevoie de Google).##

'''
1. Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
- Declara o lista cu 5 jucatori: lista_jucatori_teren
- Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
- Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
- Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
- SCHIMBARI_MAX va fi o constanta cu valoarea 3
Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
- Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe
teren
- Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
- Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori
de rezerva
- Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele
variabilelor voastre)
Daca jucatorul pe care vrem sa il schimbam nu e in teren:
- Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Altfel, afisati ecran: ‘mai aveti z schimbari’
'''

lista_jucatori_teren = ['Gabi', 'Mara', 'Ion', 'Mihai', 'Marian']
lista_jucatori_rezerva = ['Ana', 'Maya', 'Ionela']
lista_jucatori_scosi = []
schimbari_efectuate = 0
schimbari_max = 3

print(f'Echipa din teren este:', lista_jucatori_teren)
print(f'Rezerve disponibile:', lista_jucatori_rezerva)

while schimbari_efectuate < schimbari_max:
    x = input('Scoate jucator: ').capitalize()
    y = input('Adauga jucator: ').capitalize()
    if x in lista_jucatori_teren and y in lista_jucatori_rezerva:
        lista_jucatori_teren.remove(x)
        lista_jucatori_scosi.append(x)
        lista_jucatori_rezerva.remove(y)
        lista_jucatori_teren.append(y)
        schimbari_efectuate += 1
        print(f'A iesit din teren {x}, a intrat in teren {y}.\nMai ai {schimbari_max - schimbari_efectuate} schimbări.')
        print(f'Echipa din teren este:', lista_jucatori_teren)
        print(f'Jucatori scosi:', lista_jucatori_scosi)
        print(f'Rezerve disponibile:', lista_jucatori_rezerva)
    else:
        print(f'nu se poate efectua schimbarea deoarece jucătorul {x} nu e în teren sau jucatorul {y} nu e rezerva. \nMai ai {schimbari_max - schimbari_efectuate} schimbari')
else:
    print('nu mai ai schimbari')



