## RANDOM EXERCISE #####################################################################################################

old_list = [1, 2, 3]
#new_list = old_list

new_list = old_list.copy()
new_list = list(old_list)
new_list = old_list[:]

old_list[0] = 4

print(old_list)
print(new_list)


## RANDOM EXERCISE #####################################################################################################

old_list = [1, 2, 3]
new_list = old_list

for i in old_list:
    new_list = i**2
    print(new_list)

## RANDOM EXERCISE #####################################################################################################
# 1st solution
old_list = list(range(9))
print(old_list)

new_list = []

for i in old_list:
    new_list.append(i**2)

print(new_list)

#2nd solution
old_list = list(range(9))
print(old_list)

new_list = [x**2 for x in old_list]
print(new_list)

## RANDOM EXERCISE #####################################################################################################

import copy

nested_list = [[[1, 2, 3], 11, 12]]
new_list = copy.deepcopy(nested_list)
#new_list = nested_list.copy()

nested_list[0][1] = 36

print(nested_list)
print(new_list)

## RANDOM EXERCISE #####################################################################################################

list1 = list(range(0,9))
list2 = list(range(9,20))
print(list1)
print(list2)
list3 = []

for e1_l1, e1_l2 in zip(list1, list2):
    list3.append(e1_l1 + e1_l2)
print(list3)


## RANDOM EXERCISE #####################################################################################################

def dodaj(x, y):
    suma = x + y
    return suma


wynik = dodaj(2, 3)

print(wynik)

## RANDOM EXERCISE #####################################################################################################

def slowo(word, times):
    for i in range(times):
        print(word)


wynik = slowo('apple', 5)
print(wynik)


## RANDOM EXERCISE #####################################################################################################

def split_sentence_to_words(sentence):
    return sentence.split(" ")


print(split_sentence_to_words("Python day four."))