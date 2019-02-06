from Contact import Contact
from Contact import Supplier

c = Contact("Some Body", "somebody@example.net")

s = Supplier("Sup plier", "supplier@example.net")

print(c.name, c.email, s.name, s.email)

print(c.all_contacts)

#c.order("I need pliers") -- It should throw error:wq

s.order("I need pliers")
