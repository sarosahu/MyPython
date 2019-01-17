
record = ('Saroj', 'saroj@example.com', '773-555-1212', '847-555-1212')

# Starred variable used in last
name, email, *phone_numbers = record

print(name)
print(email)
print(phone_numbers)
print(type(phone_numbers))


# Starred variable used in first
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(type(trailing))
print(trailing)
print(current)

#Star syntax used in iterating over sequence of tuples

records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

#Star unpacking is useful when  combined with certain
# kinds of  string processing operations such as splitting.
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

print(uname)
print(homedir)
print(sh)

#Sometimes we might want to unpack values and throw them away.
#We can’t just specify a bare * when unpacking, but we could
#use a common throwaway variable name, such as _ or ign (ignored)
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_,year) = record
print(name)
print(year)


#Star unpacking with list processing
#However, be aware that recursion really isn’t a strong Python feature
#due to the inherent recursion limit. Thus, this below example might
#be nothing more than an academic curiosity in practice.
items = [1, 10, 7, 4, 5, 9]
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print("sum: ",sum(items))
