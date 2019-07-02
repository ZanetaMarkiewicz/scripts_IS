# EASY
# 1 ####################################################################################################################
# Przypisz do zmiennej o nazwie float_but_int wartosc dzielenia 50 / 2. Jakiego typu jest wynik
# (do sprawdzenia typu type(zmienna))?
# Sprawdz przy pomocy metody wbudowanej w otrzymany wyzej typ czy liczba jest calkowita
# (dokumentacja - dir(nazwa_zmiennej) lub help(typ)), dokumentacja Python

float_but_int = 50/2
print (type(float_but_int))


# 2 ####################################################################################################################
# (Kalkulator, albo Python) - liczba zapisana w systemie binarnym na 8 bitach - 11011010 to w systemie dziesietnym liczba:

11011010 =218
1	1	0	1	1	0	1	0
128	64	32	16	8	4	2	1
128	+64	+0	+16	+8	+0	+2	+0	=218


# 3 ####################################################################################################################
# Przypisz do 3 zmiennych pojedyncze slowa "Sun", "is", "setting", polacz je w jeden ciag znaków, ale tak,
# aby kazde slowo bylo w nowej linii, kazda nowa linia ma miec jedno
# wiecej wciecie tabulatora, tak aby wygladalo to nastepujaco:

first = "Sun"
second = "is"
third = "setting."

print(f"{first} + \n\t + {second} + \n\t + {third}")
print(f"{first}\n\t{second}\n\t\t{third}")


# MEDIUM
# 4 ####################################################################################################################
# zapoznaj sie z metoda input() w Python - wyszukaj w dokumentacji i sprawdz dzialanie. Funkcja print zachec uzytkownika,
# # aby podal liczbe, nastepnie wypisz kwadrat oraz szescian tej liczby
# # Postaraj sie o odpowiedni wyglad odpowiedzi, opisujacy uzyskane wyniki, np.
# # Szescian liczby x wynosi x^3, natomiast kwadrat x^2

x = int(input ("Podaj dowolna liczbe:"))

kwadrat = x ** 2
szescian = x ** 3
print ("Szescian liczby " + str(x) + " wynosi " + str(szescian) + ", natomiast kwadrat wynosi " + str(kwadrat))


# CHALLENGING
# 5 ####################################################################################################################
# Warunek if - przy pomocy metody input pobierz od uzytkownia wartosc temperatury. Ustaw 3 minimalne temperatury
# jako zmienne - zimna, ciepla, goraca (np. 10 stopni, 20 stopni, 30 stopni)
# i na podstawie temperatury podanej przez uzytkownika, wyswietl czy jest zimno, cieplo, czy goraco

x = int(input ("Podaj temperature:"))
zimno = 10
cieplo = 20
goraco = 30

if x <= zimno:
    print ("Na zewnatrz jest ZIMNO.")
elif x > zimno and x <= cieplo:
    print ("Na zewnatrz jest CIEPLO.")
else:
    print ("Na zewnatrz jest GORACO.")


# 6 ####################################################################################################################
# Oblicz silnie z podanej przez uzytkownika (metoda input) liczby - wyszukaj algorytm na silnie i napisz - przydadza sie
# zmienne, warunek if, operator *=

x = int(input ("Podaj dowolna liczbe:"))
silnia = 1

for i in range(1, x+1):
    silnia *= i
print(silnia)
