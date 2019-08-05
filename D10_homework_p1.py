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

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SpamSender(object):
    def __init__(self, sender_email, receiver_email, password, title, text, host, port):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.password = password
        self.title = title
        self.text = text
        self.host = host
        self.port = port

    def mail_sender(self):
        for email in self.receiver_email:
            receiver_email = email

            message = MIMEMultipart("alternative")
            message["Subject"] = self.title
            message["From"] = self.sender_email
            message["To"] = receiver_email

            text_part = MIMEText(self.text, "html")
            message.attach(text_part)

            ssl.create_default_context()
            server = smtplib.SMTP_SSL(self.host, self.port)
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, message.as_string())
            # server.quit()
