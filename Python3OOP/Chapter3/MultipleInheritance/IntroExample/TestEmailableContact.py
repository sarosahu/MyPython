from Contact import Contact
from MailSender import MailSender
from EmailableContact import EmailableContact

e = EmailableContact("Saroj Sahu", "saroj@sahu.com")
print(Contact.all_contacts)
e.send_mail("Hello, test e-mail here")
