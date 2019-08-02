import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "isa12python@gmail.com"
receiver_email = "isa12python@gmail.com"
password = "iSAforever"

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

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

# dodaj dwie reprezentacje wiadomosci - najpierw tryb HTML, potem zwykly tekst
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.login(sender_email, password)
server.sendmail(
    sender_email, receiver_email, message.as_string()
)