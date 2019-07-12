# 0 ####################################################################################################################
# jako prace domową - przejrzyj zadania - examples z folderu Trainings - przykłady nie zaczynaja sie od numeru
# oraz rozwiaz zadania z folderu Trainings (pliki zaczynajace sie od numerow)
#
# 0.1 ##################################################################################################################
# oblicz czy rok jest przestępny
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

year = input("Enter year: ")
year = int(year)

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("This is a leap year")
else:
    print(" This isn't a leap year")


# 0.2 ##################################################################################################################
# podane 3 boki trojkata, okresl
# - czy uda sie narysowac trojkata
# * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
# - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

bok_a = int(input("Podaj bok a: "))
bok_b = int(input("Podaj bok b: "))
bok_c = int(input("Podaj bok c: "))

if (bok_a < bok_b + bok_c) and (bok_b < bok_c + bok_a) and (bok_c < bok_a + bok_b ):
    print("It is possible to create triangle")
    if bok_a == bok_b == bok_c:
        print("This is equilateral triangle")
    elif bok_a == bok_b != bok_c or bok_a == bok_c != bok_b or bok_b == bok_c != bok_a:
        print("This is isosceles triangle")
    else:
        print("This is scalene triangle")


# 0.3 ##################################################################################################################
# zamiana temperatury
#     wejscie: temperatura w C lub F, np: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni" - jezeli podano w F to wypisz w C i odwrotnie
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

input_temp = (input("Enter temperature: ")).upper()

if "F" in input_temp:
    C = (int(input_temp.replace("F","")) - 32) * (5 / 9)
    print(f"Input temperature {input_temp} in C is {C}")
else:
    F = int(input_temp.replace("C","")) * (9 / 5) + 32
    print(f"Input temperature {input_temp} in F is {F}")


# 0.4 ##################################################################################################################
# obl. ilość l. parzystych i nieparzystych w zakresie

zakres = range(23746)

parzyste = 0
nieparzyste = 0


for liczba in zakres:
    if liczba % 2 == 0:
        parzyste += zakres.count(liczba)
    else:
        nieparzyste += zakres.count(liczba)


print(f"Liczb parzystych: {parzyste}, liczb nieparzystych: {nieparzyste}")


# 0.5 ##################################################################################################################
# policz samogloski i spolgloski

zdanie = input("Podaj jakieś zdanie: ")

samogloski = 0
spolgloski = 0

lista_samogl = "aeiouyąęó"

for litera in zdanie:
# tutaj nalezy napisac kod ;)


print(f"Samoglosek: {samogloski}, spółgłosek: {spolgloski}")


# 0.6 ##################################################################################################################
# fizz buzz
# wypisac liczby od 1 do 100 (włącznie)
# zamiast l. podzielnych przez 3 wypisz Fizz
# zamiast liczb podzielnych przez 5 wypisz Buzz
# zamist liczb podzielnych przez 3 i 5 wypisz FizzBuzz

zakres = range(1, 101)

for liczba in zakres:
    # tutaj nalezy napisac kod ;)


# 0.7 ##################################################################################################################
# program, ktory wypisze liczby (z zakresu 0 do 100) z ciagu Fibonacciego
# 0, 1, 1, 2, 3, 5, 8, 13, 21
# propozycja uzycia petli while - ale kazde rozwiazanie jest dobre ;)


# 0.8 ##################################################################################################################
# napisz funkcje obliczajaca pole kwadratu


# 1 ####################################################################################################################
# stwórz słownik, którego kluczem będą słowa, natomiast wartością znaczenie tych słów
# może być słownik miejskiego slangu ;)

words_dict["kasiora"] = "Opis słowa kasiora"


# 2 ####################################################################################################################
# zapisz prosta zawartosc slownika miejskiego slangu do pliku, w kazdej linii klucz - wartosc
# np kasiora - Opis slowa kasiora, w nowej linii nastepna para


# 3 ####################################################################################################################
# zapisz slownik slangu miejskiego do pliku csv, gdzie klucz (slowo) i wartosc (wyjasnienie slowa)
# beda oddzielone pionową linią pipe (|) - przyklad zapisu pliku csv w Day6\exercises\cs_example


# 4 ####################################################################################################################
# zapisz slownik slangu miejskiego jako pickle - przyklad w Day6\exercises\pickle_1.py
# odczytaj plik i sprawdz czy poprawnie zapisano dane


# 5 ####################################################################################################################
# odczytaj plik article.txt w calosci - plik umieszczony w Day5\exercises\article.txt
# pozwol uzytkownikowi na podanie slowa i policz ile razy dane slowo wystepuje w artykule
# (powiedz uzytkownikowi ile razy wystepuje)


# 6 ####################################################################################################################
# utwórz program, w ktorym uzytkownik bedzie mogl powiekszac baze slow slangu miejskiego
# na poczatku programu zaladuj slownik z pliku pickle
# (sprawdz czy plik istnieje, albo po wykonaniu zadania 4 uzyj istniejacego pliku)
# napisz program tak, aby uzytkownik mogl dodawac slowa i ich wyjasnienie, dopoki nie zechce wyjsc z programu
# (moze byc krotkie pytanie czy chcesz dodac slowo do slownika? TAK/NIE)
# na koncu programu zapisz slownik ponownie do pliku pickle, aby zapisac zmiany
