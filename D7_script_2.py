import my_modul
# from my_modul import listdir
# from my_modul import listdir as showdir
import os

print("Program wywolujacy modul")
print(30 * "=")
#print(os.listdir())
print(30 * "=")
my_modul.showdir()
print(30 * "=")

result = my_modul.showdir()
for item in result:
    print(item)
