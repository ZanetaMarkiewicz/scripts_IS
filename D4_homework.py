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
    words = sentence.split(" ")
    return words


def sort_words(words):
    words.sort()
    return words


print(sort_words(split_sentence_to_words(sentence)))


# 5 ####################################################################################################################
# (optional) Zaimportuj modul (plik) i uzyj funkcji z tego modulu
#  help(nazwa_pliku) - zadokumentuj troche kodu!
