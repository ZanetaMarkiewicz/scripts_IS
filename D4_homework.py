### PART I
# 1 ####################################################################################################################
# Napisz funkcję, która przyjmuje dowolną ilość parametrów - zaloz ze beda podawane liczbowe, funkcja ma wypisywac te
# parametry, uzywajac petli for in

def my_function(*args):
    for i in args:
        print(i)


my_function(1,2,3,4,5,6,7,8,9,100)


# 2 ####################################################################################################################
# Zmodyfikuj funkcje z zadania wyzej tak, aby na koncu wypisala sume liczb podanych do funckji

def my_function_sum(*args):
    return sum(args)


print(my_function_sum(1,2,3,4,5,6,7,8,9,100))


# 3 ####################################################################################################################
# Inside - out - napisz dwie funckje - dodawanie (np o nazwie add) oraz mnozenie dwoch liczb (np o nazwie multiply),
# nastapnie wywolaj operację multiply(add(2, 6), 2)

def add(first_number, second_number):
    add_result = first_number + second_number
    return add_result

def multiply(first, second):
    multiply_result = first * second
    return multiply_result

print(multiply(add(2,6),10))


# 4 ####################################################################################################################
# Napisz funkcję rozbijajaca zdanie na slowa (ma zwracac liste ze slowami) oraz funkcje sortujaca liste slow, nastepnie
# wywolaj sortowanie na slowach podanego przez uzytkownika zdania
# sort_words(split_sentence_to_words(sentence))

sentence = input("Podaj zdanie:")


def split_sentence_to_words(sentence):
    """ Def divides sentence to words and return them as a list of words."""
    words = sentence.split(" ")
    return words


def sort_words(words):
    """ Def orders list of words alphabetically. """
    words.sort()
    return words


print(sort_words(split_sentence_to_words(sentence)))
print(split_sentence_to_words.__doc__)
print(sort_words.__doc__)


# 5 ####################################################################################################################
# (optional) Zaimportuj modul (plik) i uzyj funkcji z tego modulu
#  help(nazwa_pliku) - zadokumentuj troche kodu!

### PART II

# 1 ####################################################################################################################
# stwórz kilka zmiennych różnych typów - int, float, boolean, string
# 2 za pomocą funkcji print() wypisz wartości powyższych zmiennych, podając ich typ (użyj funkcji type)
# pamiętaj o formatowaniu i znakach specjalnych, najlepiej aby pokazywać wartości wraz z typami zmiennych
# w nowej linii

string = 'Ala ma kota'
number = 45
floating_point = 5.2

print(f"{string} to typ: {type(string)}\n{number} to typ: {type(number)}\n{floating_point} to typ: {type(floating_point)}")


# 3 ####################################################################################################################
# Wypisz zmienną typu float - dobrym przykladem bedzie liczba 1/17
# z dokładnością do 4 miejsc po przecinku
# https://stackoverflow.com/questions/8885663/how-to-format-a-floating-number-to-fixed-width-in-python

number = 1/17

print("{:6.4f}".format(number))


# 4 ####################################################################################################################
# Indeksowanie (slajd dzien 3 od strony 4)
# stwórz nową zmienną typu string oraz zmienną pomocniczą, do której przy pomocy indeksowania,
# przypiszesz odwrócony string pierwszej zmiennej (możesz przejrzeć slajd 4 z prezentacji dnia 3 i sprawdzic np w konsoli
# które indeksowanie odwraca)

my_string = "banan"
my_string_backwords = my_string[::-1]

print(my_string,my_string_backwords)


# 5 ####################################################################################################################
# rozszerz zadanie 4 - sprawdź czy string jest palindromem

if my_string == my_string_backwords:
    print("palindrome")
else:
    print("not a palindrome")


# 6 ####################################################################################################################
# przy pomocy funkcji input() rozszerz zadanie 5 tak aby uzytkownik wpisał słowo i program powiedział,
# czy wisane slowo jest palindromem

word = input("Enter word: ")
rev_word = word[::-1]

if word == rev_word:
    print("palindrome")
else:
    print("not a palindrome")


# 7 ####################################################################################################################
# wykorzystaj funkcje input() i zagraj z uzytkownikiem programu w grę RPG
# Poinformuj użytkownika że stoi na rozdrozu - moze isc prosto, w lewo, lub w prawo
# aby pójść prosto - musi wpisać "straight", w lewo - "left", w prawo = "right"
# w zależności od wyboru ścieżki, poinformuj użytkownika kogo spotkał (dla Twojej wyobraźni sky is the limit)
# jeżeli użytkownik nie wpisał poprawnie kierunku - napisz że nie umie się grać...
# (do rozwiazania przyda się if elif else)

player_input = input("player input:")

prosto = "straight"
lewo = "left"
prawo = "right"

if player_input == prosto:
    print("You went straight & you met Gandalf")
elif player_input == lewo:
    print("You went left & you met your boss")
elif player_input == prawo:
    print("You went right & you met your mother")
else:
    print("You don't know how to play ... ")


# 8 ####################################################################################################################
# rozszerz zadanie 7 w taki sposób, aby zachęcić użytkownika jeszcze raz do wyboru ścieżki, jeżeli nie wpisał komendy
# poprawnie, (przyda się pętla while - mozesz zatrzymać skrypt ręcznie jeżeli w czasie wykonywania się zapętlił nie tak
# jak powinien)

player_input = input("player input:")

prosto = "straight"
lewo = "left"
prawo = "right"

while True:
    if player_input == prosto:
        print("You went straight & you met Gandalf")
        break
    elif player_input == lewo:
        print("You went left & you met your boss")
        break
    elif player_input == prawo:
        print("You went right & you met your mother")
        break
    else:
        print("You entered wrong instruction. Try again!")
        player_input = input("player input:")


# 9 ####################################################################################################################
# Klasa range - przy użyciu pętli for in oraz użyciu range, wypisz tylko liczby podzielne przez 7 w zakresie 0-77
# wskazówka: przyda się warunek if oraz modulo %
# 4 % 2 == 0 -> true

for number in range(0, 77):
    if number % 7 == 0:
        print(number)


# 10 ###################################################################################################################
# wygeneruj 2 listy liczb o tych samych rozmiarach, ale różnych wartościach

list_1 = list(range(1, 10))
list_2 = list(range(10, 19))

print(list_1)
print(list_2)


# 11 ###################################################################################################################
# stwórz nową listę, używając dwóch
# list z zadania 10. lista ma zawierać liczby z listy pierwszej podniesione przemnozone przez liczbę o tym samym
# indeksie z listy drugiej# [1, 2, 3]
# [3, 8, 2]
# -> [3, 16, 6]

list_3 = []

for i1, i2 in zip(list_1, list_2):
    list_3.append(i1 * i2)
print(list_3)
