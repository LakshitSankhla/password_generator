import random
ulist=[]
llist=[]
nlist=[]
slist=[]

def pass_generator(u,l,num,s):
    for i in range(u):
        Ucase=chr(random.randint(65,90))
        ulist.append(Ucase)
    for i in range(l):
        Lcase=chr(random.randint(97,122))
        llist.append(Lcase)
    for i in range(num):
        nos=chr(random.randint(48,57))
        nlist.append(nos)
    for i in range(s):
        spec_list=[random.randint(32,47),random.randint(58,64),random.randint(91,95), 123,125]
        spec_char=chr(random.choice(spec_list))
        slist.append(spec_char)

    plist=ulist+llist+nlist+slist
    random.shuffle(plist)
    password="".join(plist)
    print(password)




n=int(input("Enter Lenght of Password You Want(less than 20 characters): "))
u,l,num,s=0,0,0,0
while(u + l + num +s != n):
    u=random.randint(1,5)
    l = random.randint(1, 5)
    num = random.randint(1, 5)
    s = random.randint(1, 5)

pass_generator(u,l,num,s)


