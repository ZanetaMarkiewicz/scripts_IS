import requests
import csv
import folium

path = r"D:\!_Python_trainig\scripts_IS\airports_data.csv"

def data_download():
    data_url = 'https://raw.githubusercontent.com/infoshareacademy/isa-python12/master/Day8/exercises/airports.csv?token=AGMZVYOFLTW6SJTOMBVPTRS5HCKJ2'

    airports_data = requests.get(data_url)
    # csv_data = airports_data.content
    csv_data = airports_data.text

    with open(path, 'w') as csv_file:
        csv_file.write(csv_data)

data_download()

# tworzy base mape
map = folium.Map()

with open(path, 'r') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    for airport in data:
        # font awesome -  biblioteka otwarta
        icon = folium.Icon(icon='plane', prefix='fa', color="purple")
        #point = folium.Marker(location=[airport[5], airport[6]], tooltip=airport[1]).add_to(map)
        point = folium.Marker(location=[airport[5], airport[6]], tooltip=airport[1], icon=icon)
        map.add_child(point)

map.save("map.html")

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#tworzymy obiekt MIMEMultipart, który za nas dokona odpowiedniego utworzenia źródła maila do wysłania
msg = MIMEMultipart()

#otwieramy plik którego zawartość chcemy wysłać jako treść maila
textfile = path
with open(textfile, 'r') as fp:
   #tworzymy obiekt MIMEText w paramatrze podając zawartość pliku
   #jest to obiekt odpowiadający za treść maila
   text = MIMEText(fp.read())

#dołączamy treść maila do naszej wiadomości
msg.attach(text)

#ustawiamy nagłówki niezbędne do poprawnej wysyłki maila
#temat
msg['Subject'] = 'The contents of '
msg['From'] = 'isapy@o2.pl'
#odbiorca
msg['To'] = 'isapy@o2.pl'

#tworzymy obiekt dzięki któremy wyślemy wiadomość
#w konstruktorze podajemy adres serwera dzięki któremy będziemy wysyłać wiadomość
s = smtplib.SMTP('poczta.o2.pl')

#podany serwer wymaga uwierzytelnienia więc wywołujemy metodę do logowania
s.login('isapy@o2.pl', 'isapython')

#wywłamy wiadomość, moetoda msg.as_string() zamienia obiekt MIMEMultipart ze wszystkim załącznikami
#na wiadomość zgodną z RFC do wysłania wiadomośći
s.sendmail(msg['From'], [msg['To']], msg.as_string())

