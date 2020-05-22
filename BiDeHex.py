question_one = ""
question = ""


def question_two(x):
    q = input("Write the letter r to Reset the program or e to exit\n")
    if q == "r":
        print("\n\n\n\n\n\n\n\n\n\n\n\n")
    if q == "e":
        exit()


while question_one != "b" or question_one != "d" or question_one != "h":
    while True:
        try:
            question_one = input("What numeral system is ur number in?\nBinary = b\nDecimal = d\nHexadecimal = h\n")
            break
        except ValueError:
            print("death")

    if question_one == "b":
        ur_number = input("What is ur number?\n")
        decimal_representation = int(ur_number, 2)
        print("The Decimal value of the number is", decimal_representation)
        print("The Hexadecimal value of the number is", hex(decimal_representation))
        question_two(question)

    elif question_one == "d":
        ur_number = int(input("What is ur number?\n"))
        print("The Binary value of the number is", bin(ur_number))
        print("The Hexadecimal value of the number is", hex(ur_number))
        question_two(question)

    elif question_one == "h":
        ur_number = input("What is ur number?\n")
        print("The Decimal value of the number is", int(ur_number, 16))
        print("The Binary value of the number is", bin(int(ur_number, 16)))
        question_two(question)