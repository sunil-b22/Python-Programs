#Password Generator

import random
import string

symbol = ["!", "@", "#", "$", "%", "&", "*", "+"]

plength = int(input("Enter the length of password (min 6): "))

if plength >= 6:
    palph = int(input("Enter the no. of alphabets to be present (Should be less than or equal to {}): ".format(plength)))

    if palph <= plength:
        x = plength - palph

        pnum = int(input("Enter the no. of digits to be present (Should be less than or equal to {}): ".format(x)))

        if pnum <= x:
            rem = x - pnum

            passw=[]

            #Generating the alphabet part of password
            for i in range(0,palph):
                alp = random.choice(string.ascii_letters)
                passw.append(alp)

            #Generating the digit part of password
            for j in range(0,pnum):
                num = str(random.randrange(0,9))
                passw.append(num)

            #Generating the symbol part of password
            for k in range(0,rem):
                sym = str(random.choice(symbol))
                passw.append(sym)

            random.shuffle(passw)

            passw="".join(passw)

            print("Your password: {}".format(passw))

        else:
            print("Invalid Input")

    else:
        print("Invalid Input")

else:
    print("Invalid Input")
