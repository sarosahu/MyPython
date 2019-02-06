from Contact import Contact
from MailSender import MailSender
class EmailableContact(Contact, MailSender):
    pass
