choice_of_numeral_system = ""


def exit_or_reset(x):
    if x == "e":
        exit()


while choice_of_numeral_system != "b" or choice_of_numeral_system != "d" or choice_of_numeral_system != "h":
    while True:
        try:
            choice_of_numeral_system = input("What numeral system is your number in?\n"
                                             "Binary = b\nDecimal = d\nHexadecimal = h\n")
            break
        except ValueError:
            print("ValueError\n Restart Program")

    if choice_of_numeral_system == "b":
        ur_number = input("What's your number?\n")
        decimal_number = int(ur_number, 2)
        print("The Decimal value of the number is", decimal_number)
        print("The Hexadecimal value of the number is", hex(decimal_number))
        exit_or_reset(input("Enter the letter e to exit the program.\nEnter anything to reset the program.\n"))

    elif choice_of_numeral_system == "d":
        ur_number = int(input("What's your number?\n"))
        print("The Binary value of the number is", bin(ur_number))
        print("The Hexadecimal value of the number is", hex(ur_number))
        exit_or_reset(input("Enter the letter e to exit the program.\nEnter anything to reset the program.\n"))

    elif choice_of_numeral_system == "h":
        ur_number = input("What's your number?\n")
        print("The Decimal value of the number is", int(ur_number, 16))
        print("The Binary value of the number is", bin(int(ur_number, 16)))
        exit_or_reset(input("Enter the letter e to exit the program.\nEnter anything to reset the program.\n"))
