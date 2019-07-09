## RANDOM EXERCISE #####################################################################################################

imie = "Jola"


def zmien_imie():
    imie = "Teresa"


print(imie)

## RANDOM EXERCISE #####################################################################################################
# napisz funkcję sumujący wszystkie elementy w liscie


def my_function_sum(*args):
    """ Def returs a sum of multiple arguments"""
    return sum(args)


print(my_function_sum(1,2,3,4,5,6,7,8,9,100))
print(my_function_sum.__doc__)

## RANDOM EXERCISE #####################################################################################################
# znajdz najwiekszy / najmniejszy element w liscie - napisz dwie funkcje
# 2 sposoby - najpierw ręcznie, następnie sprytnie

testing_list = [9,10,2,4,8,6,4,25,37,48]

# 1st solution
def find_max_min1(testing_list):
    testing_list.sort()
    max = testing_list[-1]
    min = testing_list[0]
    return max, min

print(find_max_min1(testing_list))

# 2nd solution
def find_max_min2(testing_list):
    max_value = max(testing_list)
    min_value = min(testing_list)
    return max_value, min_value

print(find_max_min2(testing_list))


## RANDOM EXERCISE #####################################################################################################
#  funkcja ktory zmieni zdanie w liste wyrazow

sentence = "Ala ma kota, kot ma Ale"


def sentence_split(sentence):
    new_list = list(sentence.split(" "))
    return new_list

print(sentence_split(sentence))

## RANDOM EXERCISE #####################################################################################################
# napisz funckję przyjmujaca liste stringow,
# a zwracakaca liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
# ['abc', 'xyz', 'aba', '1221'] - odp = 2

string_list = ['dd','a','abca', 'xyz', 'aba', '1221']


def string_test(string_list):
    string_counter = 0
    for i in string_list:
        if len(i) > 2 and i[0] == i[-1]:
            string_counter += 1
    return string_counter


print(string_test(string_list))


## RANDOM EXERCISE #####################################################################################################
# program znajdujacy wartosci, ktre wystepuja tylko raz

list_a = [10,20,30,20,10,50,60,40,80,50,40]


def occurs_once(list_a):
    new_list =[]
    for i in list_a:
        if list_a.count(i) == 1:
            new_list.append(i)
    return new_list


print(occurs_once(list_a))


## RANDOM EXERCISE #####################################################################################################
# program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
# podpowiedz - del lub pop()

list_b = [10,20,30,20,10,50,60,40,80,50,40]

list_b = set(list_b)

print(list_b)


## RANDOM EXERCISE #####################################################################################################
# program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True

list_a = [10,50,60,40,80,50,40]
list_b = [10,20,30,20,10,50,60,40,80,50,40]


def list_checker(list_a):
    for i in list_a:
        if i in list_b:
            return True
    return False


print(list_checker(list_a))


## RANDOM EXERCISE #####################################################################################################
# stworz macierz (4 x 5), ktorej wszystkie komorki wypelnione sa znakiem *

def matrix():
    result = []
    for i in range(4):
        col = []
        for j in range(5):
            col.append("*")
        result.append(col)
    return result

print(matrix())


## RANDOM EXERCISE #####################################################################################################
# wybierz losowo element z listy  wskazowka - import random


## RANDOM EXERCISE #####################################################################################################
# oblicz częstość elementów w liście (ile razy) jedna wersja zwykla pętle, ify itd, druga - moze jest jakis modul gotowy???

my_list = [10,10,20,10,10,20,10,20,20,20,40,50,40,10,30,50,50,30]




## RANDOM EXERCISE #####################################################################################################

simple_dict = {1: "jeden", 2: "dwa"}

for key, value in simple_dict.items():
    print(f"pod kluczem {key} jest wartosc {value}.")

simple_dict[1] = "trzy"

for key, value in simple_dict.items():
    print(f"pod kluczem {key} jest wartosc {value}.")


## RANDOM EXERCISE #####################################################################################################

movies_dict = {2010: "AAA", 2008: "BBB", 2013: "CCC"}

for key, value in movies_dict.items():
    print(f"W roku {key} premiere mial film {value}.")