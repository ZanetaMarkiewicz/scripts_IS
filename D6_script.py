## RANDOM EXERCISE #####################################################################################################

elementy = {1: "ola", 0: "ala", 2: "eva"}

elementy[3] = "Adam"

print(elementy)
print(elementy[3])


## RANDOM EXERCISE #####################################################################################################

rekordy = [{"imie": "Adam", "nazwisko": "kowalski", "wiek": 32},
           {"imie": "Anna", "nazwisko": "nowak", "wiek": 23},
           {"imie": "Jan", "nazwisko": "nowacki", "wiek": 34},
           {"imie": "Tomasz", "nazwisko": "lato", "wiek": 43}]

dict_of_person = {}

for indeks, rekord in enumerate(rekordy):
    print(f"pod kluczem {indeks} jest wartosc {rekord}.")
    dict_of_person[indeks + 1001] = rekord

print(dict_of_person)

for key, value in dict_of_person.items():
    print(f"pod kluczem {key} jest wartosc {value}.")


## RANDOM EXERCISE #####################################################################################################

movies_dict = {2010: "AAA", 2008: "BBB", 2013: "CCC"}

movies_dict[2000] = 'Matrix'
movies_dict[2019] = ["Blue Notebook", "DDDD"]
movies_dict[2019].append("ZZZZ")

for key, value in movies_dict.items():
    print(f"W roku {key} premiere mial film {value}.")

for key, value in movies_dict.items():
    print(f"{key}\n\t{value}")


## RANDOM EXERCISE #####################################################################################################

list_of_movies = ["Obcy 3", "Terminator", "Dawno temu w trawie"]

with open("D:\!_Python_trainig\scripts_IS\movies.txt", "w") as plik:
    for movie in list_of_movies:
        plik.write(movie + "\n")
# plik.writelines()


## RANDOM EXERCISE #####################################################################################################

movies_dict = {}

movies_dict[2000] = ["Matrix"]
movies_dict[2019] = ["Blue Notebook", "DDDD"]
movies_dict[2019].append("ZZZZ")

with open("D:\!_Python_trainig\scripts_IS\movies.txt", "w") as plik:
    for key, value in movies_dict.items():
        plik.write(str(key) + "\n")
        for movie in value:
            plik.write(f"\t{movie}\n")


## RANDOM EXERCISE #####################################################################################################

try:
    zmienna = 1 / 0
except ZeroDivisionError:
    print("Wystapil blad, dzielenie przez zero")
else:
    print("Nie wystapil wyjatek")
finally:  # wykona sie zawsze
    print("zakonczenie programu")
