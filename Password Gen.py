from random import *

symbol_list = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
               "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ",", ".", "-", ";", ":", "_", "+", "*", "1", "2", "3",
               "4", "5", "6", "7", "8", "9", "0", "!", "§", "$", "%", "&", "/", "(", ")", "=", "?", "[", "]", "Ü", "ü",
               "Ö", "ö", "ä", "Ä")
container = ""
counter = 0
password = ""
want_password = input("Need a new password (y/n)?: ")

if want_password == "y":
    while True:
        try:
            len_of_password = int(input("How many characters should it have from 8 to 25?: "))
            break
        except ValueError:
            print("Only numbers!\nTry again.")

    while len_of_password < 8 or len_of_password > 25:
        print("I said from 8-25.")
        while True:
            try:
                len_of_password = int(input("How many characters should it have from 8 to 25?: "))
                break
            except ValueError:
                print("Only numbers!\nTry again.")

    while len_of_password >= 8 or len_of_password <= 25:
        while len_of_password > counter:
            counter = counter + 1
            symbol_picker = randint(0, 87)
            container = symbol_list[symbol_picker]
            password = password + container
        print(f"This is your new password: {password}")
        exit(input("Don`t forget it!\nPress Enter to exit"))

while want_password == "n":
    (print(
        "What are you doing on computer?\nGo outside, so beautiful, RARGH!!!\nDone."))
    exit(input("Press Enter to exit."))

while want_password != "y" or want_password != "n":
    print("Invalid only y and n.")
    want_password = input("Yes or no ? (y/n)?: ")
    if want_password == "y":
        while True:
            try:
                len_of_password = int(input("How many characters should it have from 8 to 25?: "))
                break
            except ValueError:
                print("Only numbers!\nTry again.")

        while len_of_password < 8 or len_of_password > 25:
            print("I said from 8-25.")
            while True:
                try:
                    len_of_password = int(input("How many characters should it have from 8 to 25?: "))
                    break
                except ValueError:
                    print("Only numbers!\nTry again.")

        while len_of_password >= 8 or len_of_password <= 25:
            while len_of_password > counter:
                counter = counter + 1
                symbol_picker = randint(0, 87)
                container = symbol_list[symbol_picker]
                password = password + container
            print(f"This is your new password: {password}")
            exit(input("Don`t forget it!\nPress Enter to exit"))

    while want_password == "n":
        (print("What are you doing on computer?\nGo outside, so beautiful, RARGH!!!\nDone."))
        exit(input("Press Enter to exit."))
