import random

def normal():
    n_list = ['a','s','r','m','g','i','o','3']
    select = random.choice(n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(n_list)
    print("your password is " + select)
def strong():
    n_list = ['a', 's', 'r', 'm', 'g', 'i', 'o', '3','2','5','8','@','N','T','I','O','K']
    select = random.choice(n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(
        n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(n_list)
    print("your password is " + select)
def anti_hack():
    n_list = ['a', 's', 'r', 'm', 'g', 'i', 'o', '3', '2', '5', '8', '@', 'N', 'T', 'I', 'O', 'K','@','Z','X']
    select = random.choice(n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(
        n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(
        n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(n_list)
    print("your password is " + select)
def GOD():
    n_list = ['a', 's', 'r', 'm', 'g', 'i', 'o', '3', '2', '5', '8', '@', 'N', 'T', 'I', 'O', 'K','@','Z','X','p','v','m','g','@','3','9']
    select = random.choice(n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(
        n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(
        n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(n_list) + random.choice(n_list)
    print("your password is " + select)
print("Welcome to password generator")
while True:
    print('''
    normal pass >> 1
    strong pass >> 2
    anti hack pass >> 3
    GOD PASS >> 4''')
    user = input(">> ")
    if user == "1":
        normal()
    elif user == "2":
        strong()
    elif user == "3":
        anti_hack()
    elif user == "4":
        GOD()
    else:
        print("plz enter password you want!")