#Guess the number game

import random

num = random.randrange(0,100)
for i in range(4,-1,-1):
    a=int(input("Guess the number between 0 to 100: "))
    print(a)
    if a == num:
        print("You won, the number was: {} ".format(num))
        exit()
    elif a > num:
        print("Guess lower")
    else:
        print("Guess higher")
    print("You have {} guesses remaining".format(i))
print("You lost, the number was: {}".format(num))



