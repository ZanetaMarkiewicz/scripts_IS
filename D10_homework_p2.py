from D10_homework_p1 import SpamSender

receiver_email = ["isa12python@gmail.com", "zaneta.markiewicz.0906@gmail.com"]

text = """\
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

test_email = SpamSender("isa12python@gmail.com", "isa12python@gmail.com", "iSAforever", "H10", text, "smtp.gmail.com",
                        465)
test_email.mail_sender()

print("Message has been correctly sent.")
