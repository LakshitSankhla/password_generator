import random
uList=[]        #list to store uppercase characters
lList=[]        #list to store lowercase characters
nList=[]        #list to store numbers
sList=[]        #list to store special characters

def pass_generator(u,l,num,s):
    for i in range(u):
        uCase=chr(random.randint(65,90))
        uList.append(uCase)
    for i in range(l):
        lCase=chr(random.randint(97,122))
        lList.append(lCase)
    for i in range(num):
        nos=chr(random.randint(48,57))
        nList.append(nos)
    for i in range(s):
        spec_list=[random.randint(32,47),random.randint(58,64),random.randint(91,95), 123,125]
        spec_char=chr(random.choice(spec_list))
        sList.append(spec_char)

    pList=uList+lList+nList+sList       #concatenating all the other lists into a single one
    random.shuffle(pList)               #randomly shuffling the list items
    password="".join(pList)             #converting the list into a string
    print(password)




n=int(input("Enter Lenght of Password You Want(less than 20 characters): "))
u,l,num,s=0,0,0,0               
while(u + l + num + s != n):        #randomly selecting number of uppercase, lowercase, numbers and special characters
    u = random.randint(1,5)
    l = random.randint(1, 5)
    num = random.randint(1, 5)
    s = random.randint(1, 5)

pass_generator(u,l,num,s)
