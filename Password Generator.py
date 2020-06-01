from random import *

container = ""
counter = 0
password = ""
symbol_list = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
               "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "{",
               "}", "(", ")", "[", "]", "#", ":", ";", "^", ",", ".", "?", "!", "|", "&", "_", "'", "~", "@", "$", "%",
               "/", "=", "+", "-", "`")
while True:
    try:
        len_of_password = int(input("How many characters should your new password have?\n"
                                    "Choose a number between 8 to 72?: "))
        break
    except ValueError:
        print("Only numbers!\nTry again.")

while len_of_password < 8 or len_of_password > 72:
    print("I said from 8-72.")
    while True:
        try:
            len_of_password = int(input("How many characters should your new password have?\n"
                                        "Choose a number between 8 to 72?: "))
            break
        except ValueError:
            print("Only numbers!\nTry again.")

if 8 <= len_of_password <= 72:
    while len_of_password > counter:
        counter = counter + 1
        symbol_picker = randint(0, 89)
        container = symbol_list[symbol_picker]
        password = password + container
    print(f"This is your new password: {password}")
    exit(input("Don`t forget it(write it down)!\nPress Enter to exit"))
