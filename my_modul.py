import os

# Wyświetl:

# Katalog: __pycache__
# Katalog: .idea
# Plik: test.py

list = os.listdir()


def showdir():
    if len(list) == 0:
        return "Katalog jest pusty"

    list2 = []

    for item in list:
        if os.path.isfile(item):
            list2.append("Plik: " + item)
        elif os.path.isdir(item):
            list2.append("Katalog: " + item)
    return list2


#2nd soultion

# new_list = ""
#
#
# def listdir():
#     for item in list:
#         if os.path.isfile(item):
#             new_list += f"Plik: {item}\n)"
#         elif os.path.isdir(item):
#             new_list += f"Katalog: {item}\n)"
#     return new_list
