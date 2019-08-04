# napisac klasę o nazwie np SpamSender w oddzielnym pliku - wykorzystać kod z Day10\exercises\mail.py
# SpamSender w konstruktorze powinien mieć możliwość podania adresu email i hasła do skrzynki pocztowej,
# z ktorej bedzie wysylany spam
# nastepnie nalezy stworzyc metodę, która będzie umożliwiała wysyłąnie maila (w formacie HTML) -
# przykład wysłania prostej wiadomości HTML w wyżej wymienionym pliku
# do danego odbiorcy
# najlepiej rozbić projekt na dwa pliki - jeden w ktorym bedziemy przechowywac klase, drugi w ktorym bedziemy
# wysylac wiadomości SPAM# jako rozszerzenie zadania utworzyć listę emaili do których należy wysłać wiadomość SPAM,
# i przy użyciu pętli wysłać wiadomość do wszystkich maili z listy :slightly_smiling_face:
# jest tez w pracach domowych na repozytorium

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create secure connection with server and send email


class SpamSender:
    def __init__(self, sender_email, receiver_email, password):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.password = password

    def mail_sender(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = "H10"
        message["From"] = self.sender_email
        message["To"] = self.receiver_email

        text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""
        html = """\
        <html>
          <body>
            <p>Hi,<br>
               How are you?<br>
               <a href="https://infoshareacademy.com">InfoShare Academy</a> 
               has many great courses.
            </p>
          </body>
        </html>
        """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        print("aaaaa")
        print(text)
        print(message)
        print(part1)


        # dodaj dwie reprezentacje wiadomosci - najpierw tryb HTML, potem zwykly tekst
        message.attach(part1)
        message.attach(part2)

        # context = ssl.create_default_context()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        server.login(self.sender_email, self.password)
        server.sendmail(self.sender_email, self.receiver_email, message.as_string())

