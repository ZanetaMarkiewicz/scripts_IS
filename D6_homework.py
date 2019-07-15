# from Trainings #######################################################################################################
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
l_samoglosek = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
l_spolglosek = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z","B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
samogloski = 0
spolgloski = 0

for litera in zdanie:
    if litera in l_samoglosek:
        samogloski += 1
    elif litera in l_spolglosek:
        spolgloski += 1
    else:
        print("To nie jest spolgloska ani samogloska. ")

print(f"Samoglosek: {samogloski}, spółgłosek: {spolgloski}")


# 0.6 ##################################################################################################################
# fizz buzz
# wypisac liczby od 1 do 100 (włącznie)
# zamiast l. podzielnych przez 3 wypisz Fizz
# zamiast liczb podzielnych przez 5 wypisz Buzz
# zamist liczb podzielnych przez 3 i 5 wypisz FizzBuzz

zakres = range(1, 101)

for liczba in zakres:
    if (liczba % 3 == 0) and (liczba % 5 != 0):
        print(liczba, "Fizz")
    elif (liczba % 5 == 0) and (liczba % 3 != 0):
        print(liczba, "Buzz")
    elif (liczba % 3 == 0) and (liczba % 5 == 0):
        print(liczba, "FizzBuzz")
    else:
        print(liczba, "Not Fizz or Buzz")


# 0.7 ##################################################################################################################
# program, ktory wypisze liczby (z zakresu 0 do 100) z ciagu Fibonacciego
# 0, 1, 1, 2, 3, 5, 8, 13, 21
# propozycja uzycia petli while - ale kazde rozwiazanie jest dobre ;)

fibonaccie_list = []

for i in range(0,100):
    if i == 0:
        fibonaccie_list.append(i)
    elif i == 1:
        fibonaccie_list.append(i)
    elif i == 2:
        fibonaccie_list.append(1)
    else:
        i = fibonaccie_list[-1] + fibonaccie_list[-2]
        fibonaccie_list.append(i)

print(fibonaccie_list)


# 0.8 ##################################################################################################################
# napisz funkcje obliczajaca pole kwadratu

bok = int(input("Podaj bok kwadratu: "))


def pole_kwadratu(bok):
    pole = bok**2
    return pole


print("Pole kwadratu wynosi: ", pole_kwadratu(bok))


# from homework_3.py ###################################################################################################
# 1 ####################################################################################################################
# stwórz słownik, którego kluczem będą słowa, natomiast wartością znaczenie tych słów
# może być słownik miejskiego slangu ;)

words_dict = {}

words_dict["kasiora"] = "Potoczne okreslenie pieniedzy"
words_dict["bandzior"] = "Osoba majaca konflikt z prawem"
words_dict["zlotowa"] = "Potoczne okreslenie taxowkarza"

print(words_dict)


# 2 ####################################################################################################################
# zapisz prosta zawartosc slownika miejskiego slangu do pliku, w kazdej linii klucz - wartosc
# np kasiora - Opis slowa kasiora, w nowej linii nastepna para

with open("D:\!_Python_trainig\scripts_IS\words_dict.txt", "w") as plik:
    for key, value in words_dict.items():
        plik.write(str(key) + " - " + str(value) + "\n")


# 3 ####################################################################################################################
# zapisz slownik slangu miejskiego do pliku csv, gdzie klucz (slowo) i wartosc (wyjasnienie slowa)
# beda oddzielone pionową linią pipe (|) - przyklad zapisu pliku csv w Day6\exercises\cs_example

import csv

with open("D:\!_Python_trainig\scripts_IS\words_dict.csv", newline='', mode="w") as csv_plik:
        writer = csv.writer(csv_plik, delimiter='|')
        for key, value in words_dict.items():
            writer.writerow([key, value])


# 4 ####################################################################################################################
# zapisz slownik slangu miejskiego jako pickle - przyklad w Day6\exercises\pickle_1.py
# odczytaj plik i sprawdz czy poprawnie zapisano dane

import pickle

with open("D:\!_Python_trainig\scripts_IS\words_dict.pckl", "wb") as pckl_plik:
    pickle.dump(words_dict, pckl_plik)

odczyt_slownika = None

with open("D:\!_Python_trainig\scripts_IS\words_dict.pckl", "rb") as pckl_plik:
    odczyt_slownika = pickle.load(pckl_plik)

print(odczyt_slownika)


# 5 ####################################################################################################################
# odczytaj plik article.txt w calosci - plik umieszczony w Day5\exercises\article.txt
# pozwol uzytkownikowi na podanie slowa i policz ile razy dane slowo wystepuje w artykule
# (powiedz uzytkownikowi ile razy wystepuje)

slowo = input("Podaj slowo: ")
liczba_wystapien = 0

with open(r"D:\!_Python_trainig\scripts_IS\article.txt", "r") as art_plik:
    article_content = art_plik.read()
    print(article_content)
    if slowo in article_content:
        liczba_wystapien = article_content.count(slowo)
        print(liczba_wystapien)
    print(f"Slowo -{slowo}- wystapilo {liczba_wystapien} razy.")


# 6 ####################################################################################################################
# utwórz program, w ktorym uzytkownik bedzie mogl powiekszac baze slow slangu miejskiego
# na poczatku programu zaladuj slownik z pliku pickle
# (sprawdz czy plik istnieje, albo po wykonaniu zadania 4 uzyj istniejacego pliku)
# napisz program tak, aby uzytkownik mogl dodawac slowa i ich wyjasnienie, dopoki nie zechce wyjsc z programu
# (moze byc krotkie pytanie czy chcesz dodac slowo do slownika? TAK/NIE)
# na koncu programu zapisz slownik ponownie do pliku pickle, aby zapisac zmiany

import pickle
import os

path = "D:\!_Python_trainig\scripts_IS\words_dict.pckl"

if os.path.isfile(path):
    with open(path, "rb") as pckl_plik:
        words_dict = pickle.load(pckl_plik)
else:
    print("Plik nie istnieje!")

zapytanie = (input("Czy chcesz dodac wpis do slownika?")).upper()

if zapytanie == "TAK":
    klucz = input("Podaj klucz: ")
    wartosc = input("Podaj wartosc: ")
    words_dict[klucz] = wartosc
else:
    print("niepoprawny input")

with open(path, "wb") as pckl_plik:
    pickle.dump(words_dict, pckl_plik)