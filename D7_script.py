import os

# wyswietla zawartosc katalowu w jakim jestesmy
#     # os.path.isdir()
#     # os.path.isfile()

path = r"D:\!_Python_trainig\self_training\venv\Scripts\python.exe D:/!_Python_trainig/scripts_IS/"

list = []

# bledny zapis trzeba tu wlozyc wyjatek
# if (list[0]):
#     print("Error")
#     exit()

if len(list) == 0:
    print("Katalog jest pusty 1.")

if not list:
    print("Katalog jest pusty 2.")

# trzeci przyklad nie zadziala bo lista nie jest type boolen
if list[0] is False:
    print("Katalog jest pusty 3.")


try:
    list[0]
    10/0
except IndexError:
    print("Error, katalog jest pusty.")
    exit()
except ZeroDivisionError:
    print("Nie dziel przez zero.")
    exit()
except:
    print("Nieznany mi blad.")
    exit()


for item in os.listdir():
    if os.path.isfile(item):
        print(f"Plik: {item}")
    elif os.path.isdir(item):
        print(f"Katalog: {item}")
