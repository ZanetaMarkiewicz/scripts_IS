# 1 ####################################################################################################################
# Napisz program analogiczny do powyższego (nie przejmuj się jeżeli nie rozumiesz pierwszej linii
# po prostu ją przepisz), gdzie podasz 3 liczby oraz wypiszesz sumę trzech podanych liczb

from sys import argv

program_name, first_arg, second_arg, third_arg = argv
# 1st SOLUTION
print(f"First argument: {first_arg}, drugi {second_arg}, trzeci: {third_arg}")
# 2nd SOLUTION
print(int(first_arg) + int(second_arg) + int(third_arg))


# 2 ####################################################################################################################
# Napisz program w którym podasz jako pierwszy argument zdanie, a drugi argument liczbę
# oznaczającą ile razy to zdanie powtórzyć. Wypisz tyle razy to zdanie – użyj pętli for in oraz klasy
# range

zdanie = "Ala ma kota"
liczba_powtorzean = 5

for i in range(liczba_powtorzean):
    print(zdanie)


# 3 ####################################################################################################################
# Czytanie plików:
# # Przeczytaj tekst: https://realpython.com/read-write-files-python/
# # Oraz poćwicz odczytywanie danych z pliku – pamiętaj żeby plik był umieszczony najlepiej w tym
# # samym miejscu co uruchamiany program, w przeciwnym wypadku podaj pełną ścieżkę do pliku

# 1st SOLUTION
file = open('D3_HOMEWORK.txt')
file_content = file.read()
print(file_content)
print(file.tell())

print('File closed? {}'.format(file.closed))
if not file.closed:
    file.close()
print('File closed? {}'.format(file.closed))

# 2nd SOLUTION
with open('D3_HOMEWORK.txt') as file:
    for line in file:
        print(line)
print('File closed? {}'.format(file.closed))