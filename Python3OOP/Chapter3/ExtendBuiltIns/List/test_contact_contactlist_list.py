from Contact import Contact

c1 = Contact("John A", "john@example.com")
c2 = Contact("John B", "john@example.com")
c3 = Contact("Jenna C", "jeena@example.com")

c_list = [c.name for c in Contact.all_contacts.search('John')]

print(c_list)
