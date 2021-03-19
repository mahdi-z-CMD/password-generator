import random
import time
def bot():
    print("-----------------")
    print("Hint number in range 1,10")
    timer = 5
    while True:
        if timer == 0:
            break
        print("game start in " + str(timer))
        time.sleep(0.5)
        timer -= 1
    lis = list(range(1, 11))
    num = random.choice(lis)
    lose = 0
    while True:
        if lose == 3:
            print("--------------")
            print("oh you lose :(")
            print("--------------")
            print("correct number is " + str(num))
            break
        pl = input("enter number you think is >> ")
        if int(pl) == num:
            print("----------")
            print("YOU WIN :)")
            print("----------")
            break
        elif int(pl) < num:
            print("number is biger")
            lose += 1
        elif int(pl) > num:
            print("number is smaller")
            lose += 1


def player():
    print("-----------------")
    print("Hint number in range 1,10")
    get = input("enter number >> ")
    get = int(get)
    while True:
        if get >= 11:
            print("OUT OF RANGE !")
            get = input("enter number >> ")
            get = int(get)
        else:
            break
    timer = 5
    while True:
        if timer == 0:
            break
        print("game start in " + str(timer))
        time.sleep(0.5)
        timer -= 1
    lose = 0
    while True:
        if lose == 3:
            print("--------------")
            print("oh you lose :(")
            print("--------------")
            break
        pl = input("enter number you think is >> ")
        if int(pl) == get:
            print("YOU WIN :)")
            break
        elif int(pl) < get:
            print("number is biger")
            lose += 1
        elif int(pl) > get:
            print("number is smaller")
            lose += 1

while True:
    print('''
    play with bot >> 1
    play with friend >> 2
    ''')
    want = input(">> ")
    if want == "1":
        bot()
    elif want == "2":
        player()
    else:
        print("plz enter mode you want!")