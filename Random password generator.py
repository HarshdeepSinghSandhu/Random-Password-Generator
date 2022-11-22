import random
len=(input("Enter length of the password: "))

def passwd_generator():
    passwd=''
    lc="abcdefghijklmnopqrstuvwxyz"
    uc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num="1234567890"
    char="!@#$%^&*()_+{}:?,./;[]=-"
    all=lc+uc+num+char
    lcheck=False
    ucheck=False
    ncheck=False
    ccheck=False
    for i in range(len):
        passwd=passwd+random.choice(all)
    for i in passwd:
        if i in lc:
            lcheck=True
        elif i in uc:
            ucheck=True
        elif i in num:
            ncheck=True
        elif i in char:
            ccheck=True
    if lcheck==True and ucheck==True and ncheck==True and ccheck==True:
        print(passwd)
    else:
        passwd_generator()
if len.isnumeric():
    len=int(len)
    while len<12:
        len=int(input("Enter a valid  length: "))
    passwd_generator()
else:
    while len.isnumeric:
        len=input("please enter numeric value only :")
        if len.isnumeric():
            len=int(len)
            while len < 12:
                len = int(input("Enter a valid  length: "))
            passwd_generator()
            break




