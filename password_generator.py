import random
ulist=[]
llist=[]
nlist=[]
slist=[]

for i in range(3):
    Ucase=chr(random.randint(65,90))
    ulist.append(Ucase)
for i in range(3):
    Lcase=chr(random.randint(97,122))
    llist.append(Lcase)
for i in range(2):
    nos=chr(random.randint(48,57))
    nlist.append(nos)
for i in range(2):
    spec_list=[random.randint(32,47),random.randint(58,64),random.randint(91,95), 123,125]
    spec_char=chr(random.choice(spec_list))
    slist.append(spec_char)

plist=ulist+llist+nlist+slist
random.shuffle(plist)
password="".join(plist)
print(password)




#n=int(input("Enter Lenght of Password You Want: "))



