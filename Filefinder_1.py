import os
import string
import pprint

question_one = ""
searched_file = ""
path_container = []
choice_list = []
choice_list_dict = {}
users_file_choice = ""
available_drives = ['%s:\\' % d for d in string.ascii_uppercase if os.path.exists('%s:\\' % d)]


def file_search_process(x):
    for r, d, f in os.walk(x):
        if searched_file in f:
            path_container.append(os.path.join(r, searched_file))
            for x in path_container:
                choice_list.append(x)
            for i in range(len(choice_list)):
                choice_list_dict[i] = choice_list[i]


def open_read_file(x):
    file_target = open(x, 'r')
    content_container = file_target.readlines()
    for line in content_container:
        print(line.strip())


def root_paths(q):
    for i in available_drives:
        file_search_process(i)


while question_one != "y" or question_one != "n":
    while True:
        try:
            question_one = input("Do you want to search for a file? (yes = y, no = n)\n")
            break
        except ValueError:
            print("Bruh")

    while question_one == "y":
        if True:
            try:
                searched_file = input("Put in the files name?: ")
                print("Rooting...")
                root_paths(available_drives)
                while choice_list_dict:
                    if True:
                        pprint.pprint(choice_list_dict, indent=4)
                        print("\nRooting Finished.")
                        try:
                            users_file_choice = int(input("Choose a number from above: "))
                            if users_file_choice not in choice_list_dict.keys():
                                print("Please use a numeral value in range.")
                            if users_file_choice in choice_list_dict.keys():
                                if True:
                                    print("Pls wait for the reading process...\n")
                                    open_read_file(choice_list_dict[users_file_choice])
                                exit(input("\nFinished reading.\nPress enter to exit program. "))

                        except ValueError:
                            print("Please use a numeral value.")
                if not choice_list_dict:
                    print("No such file found.\nTry again.")
            except TypeError:
                print("death")

    if question_one == "n":
        print("OK...?\n Bye.")
        exit(print("Closing program. "))

