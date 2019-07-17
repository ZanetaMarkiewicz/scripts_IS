# blad
grupa = ["mlody","sredni","dojrzaly"]
wiek = 30

def wiek_check(wiek):
    if wiek < 30:
        grup_o = grupa[0]
    elif 30 <= wiek < 60:
        grup_o = grupa[1]
    else:
        grup_o = grupa[2]

print(wiek_check())
print(grup_o)


# with open(r"D:\!_Python_trainig\article.txt", "a") as art_plik:
#     article_content = art_plik.read()
#     print(article_content)
#
# # index = 0

# for litera in 'Kotek':
#     print("litera {} to {}".format(index, litera))
#     break
#     index += 1
# print(index)

# a = 5
# b = 6
# a == 7
# # b = 8
# #
# # print(a)
#
# imie = "Kamil"
#
# if imie[0].isupper() and not imie[-1].isupper():
#     print("Ala ma kota")
# elif imie == "Kamila":
#     print("Kamila ma psa")
# else:
#     print("tttt")


# wynik = 3
# a = ["ala", "jeden", wynik]
# wynik = 43
# b = a.copy()
# a.append('Ola')
#
# print(a)
# print(b)

# i = 100
# while i >= 100:
#     print(i)
#
# i -= 1
# print(i)

# osoby = {0: "Ola"}
# osoby.update({4:"Ala"})
# print(osoby)


# imie = "Joanna"
# print(imie[6])

# imie = "ola"
#
# def duza(imie="ala"):
#     imie = imie.capitalize()
#     return imie
#
# print(duza())

#
# for i in range(0, 99, 33):
#     print(i)

# blad
nazwisko = "Kowalski"
print(nazwisko[1:7:2])

# listb = list('lista')
# print(listb)