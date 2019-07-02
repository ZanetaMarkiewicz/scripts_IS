## RANDOM EXERCISE #####################################################################################################
zdanie = (input("Podaj zdanie:")).lower()


if zdanie[0] == "a": #zdanie[0].lower()
    print("Słowo zaczyna sie od pierwszej litery alfabetu.")
elif zdanie[0] == "z": #zdanie[0].lower()
    print("Słowo zaczyna sie od ostatniej litery alfabetu.")
else:
    print("Słowo zaczyna się od innej litery alfabetu niz a czy z.")


## RANDOM EXERCISE #####################################################################################################
zdanie = "Ala ma kota"

if "Ala" in zdanie:
    print("True")


## RANDOM EXERCISE #####################################################################################################
lista = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
        ]
print(lista[1][2])
print(lista[1:])


## RANDOM EXERCISE #####################################################################################################
repeatHowManyTimes = int(input("Please tell me how many times to repeat..."))

for index in range(repeatHowManyTimes):
   print("Hello, it's me")
   print(index)


## 0 ###################################################################################################################
# przypisz do zmiennej o odpowiedniej nazwie nazwy miesiaca (January, February) - mozna uzyc skrotow Jan, Feb itd...
# wypisz nazwy miesiaca funkcja print()
# nazwy miesiaca musza byc oddzielone enterem (znak specjalny \n)

miesiace = ["Jan","Feb","March","April","May","Jun","July","August","September","October","November","December"]

for i in miesiace:
    print(i, "\n")


## 1 ###################################################################################################################
# wypisz co druga literę z napisu - uzyj petli for:
# text = "Python is a fantastic snake"

text = "Python is a fantastic snake"

for i in text:
    print(text[::2])
    break


## 1.1 #################################################################################################################
# skrot - przeczytaj https://docs.python.org/release/2.3.5/whatsnew/section-slices.html
# i wypisz co druga litere, tym razem w krotszy sposob

text = "Python is a fantastic snake"
print(text[::2])


## 1.2 #################################################################################################################
# wypisz teraz co trzecią literę

text = "Python is a fantastic snake"
print(text[::3])


## 2 ###################################################################################################################
# wyszukaj w dokumentacji jak rozbić powyższy tekst na listę słów a nastepnie wydrukuj ta liste (for slowo in lista)
# you need to use method on text to seperate words
# word_list = text.?
# for word in word_list:
# you need to print here

text = "Python is a fantastic snake"
words = text.split()

for i in words:
    print(i)


## 3 ###################################################################################################################
# zmien program z punktu drugiego tak, aby uzytkownik sam wpisal jakis tekst, ktory program mu rozbije na liste slow

text = input("Podaj zdanie:")
words = text.split()

for i in words:
     print(i)


## RANDOM EXERCISE #####################################################################################################

text = "Python is fantastic snake"
how_many_chars = len(text)

list_of_indexes = range(0,how_many_chars,2)

for index in list_of_indexes:
#    print(text[index])
    print(index,text[index])
#    print(text[index], end="")


## RANDOM EXERCISE #####################################################################################################

months = ["Jan","Feb","March","April"]

for index, value in enumerate(months):
    print(f"Na indexie {index} znajduje sie miesiac {value}")






