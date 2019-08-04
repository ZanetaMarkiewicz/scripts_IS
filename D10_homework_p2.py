from D10_homework_p1 import SpamSender

test_email = SpamSender
# test_email = SpamSender("isa12python@gmail.com", "isa12python@gmail.com", "iSAforever")
test_email.sender_email = "isa12python@gmail.com"
test_email.receiver_email = "isa12python@gmail.com"
test_email.password = "iSAforever"
print("wiadomosc zostala wyslana")
# receiver_email = SpamSender("isa12python@gmail.com")
# password = SpamSender.("iSAforever")