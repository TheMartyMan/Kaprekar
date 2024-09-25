import os
import sys
import random
import signal

greeting4 = "\n---------------- Kaprekar 4 jegyű számokkal ----------------\n Mindenképp eljutunk a 6174-ig, legfeljebb 7 iteráció alatt.\n\n"
greeting3 = "\n---------------- Kaprekar 3 jegyű számokkal ----------------\n Mindenképp eljutunk a 495-ig, legfeljebb 6 iteráció alatt.\n\n"

clear = lambda: os.system('cls')


def signal_handler(sig, frame):
    print("\nA programot a felhasználó megszakította.\n")
    sys.exit()


signal.signal(signal.SIGINT, signal_handler)



def generateNum(length):
    if (length == 4):
        while True:
            number = random.randint(1000, 9999)
            if len(set(str(number))) > 1:
                return number
    else:
        while True:
            number = random.randint(100, 999)
            if len(set(str(number))) > 1:
                return number



def sortDigits(number):
    digits = sorted(str(number))
    descending = int(''.join(digits[::-1]))
    ascending = int(''.join(digits))
    return ascending, descending



def Kaprekar(length, base):
    if (length == 4):
        i = 1
        while base != 6174:

            ascendingNumber, descendingNumber = sortDigits(base)

            if (len(str(base)) == 4):
                base = descendingNumber - ascendingNumber
                if (len(str(base)) < 4):
                    base = "0" + str(base)
            
            print(str(i) + ". iteráció:", descendingNumber, "-", ascendingNumber, "=", base)

            
            if (i > 7):
                print("\n8. iteráció: Megdöntöttük a 4 jegyű Kaprekar állandót, vagy hiba történt.\n(Az utóbbi valószínűbb)\n")
                sys.exit()

            i = i + 1

            input()

        print ("Innentől 7641 – 1467 = 6174 lesz minden iteráció!\n")

    else:
        i = 1
        while base != 495:

            ascendingNumber, descendingNumber = sortDigits(base)

            if (len(str(base)) == 3):
                base = descendingNumber - ascendingNumber
                if (len(str(base)) < 3):
                    base = "0" + str(base)
            
            print(str(i) + ". iteráció:", descendingNumber, "-", ascendingNumber, "=", base)


            if (i > 6):
                print("\n7. iteráció: Megdöntöttük a 3 jegyű Kaprekar állandót, vagy hiba történt.\n(Az utóbbi valószínűbb)\n")
                sys.exit()

            i = i + 1

            input()
        print ("Innentől 954 – 459 = 495 lesz minden iteráció!\n")


if __name__ == "__main__":

    if len(sys.argv) > 2:

        if(sys.argv[1] == "4"):
            clear()
            if(sys.argv[2] == "random"):
                base = generateNum(4)
                print (greeting4, "\nA generált szám:", base)
                Kaprekar(4, base)

            elif (sys.argv[2].isnumeric() and len(sys.argv[2]) == 4 and sys.argv[2][0] != "0" and len(set(sys.argv[2])) > 1):
                base = int(sys.argv[2])
                print (greeting4, "\nA megadott szám:", base)
                Kaprekar(4, base)

            else:
                print("\n",sys.argv[2] + ": Nem érvényes 4 jegyű egész szám, vagy nincs 2 különböző számjegye!\n")

        elif(sys.argv[1] == "3"):
            clear()
            if(sys.argv[2] == "random"):
                base = generateNum(3)
                print (greeting3, "\nA generált szám:", base)
                Kaprekar(3, base)

            elif (sys.argv[2].isnumeric() and len(sys.argv[2]) == 3 and sys.argv[2][0] != "0" and len(set(sys.argv[2])) > 1):
                base = int(sys.argv[2])
                print (greeting3, "\nA megadott szám:", base)
                Kaprekar(3, base)

            else:
                print("\n",sys.argv[2] + ": Nem érvényes 3 jegyű egész szám, vagy nincs 2 különböző számjegye!\n")
        else:
            print("\nAz első argumentum 3 vagy 4 lehet!\n")
    else:
        print("\nHasználat: Kaprekar.py <3 vagy 4> <random vagy 3 jegyű szám vagy 4 jegyű szám>\n")
        sys.exit()