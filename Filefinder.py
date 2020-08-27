import os, string as st, pprint as pp

searched_file = ""
path_container = []
choice_list = []
choice_list_dict = {}
users_file_choice = ""
available_drives = ['%s:\\' % d for d in st.ascii_uppercase if os.path.exists('%s:\\' % d)]
step = "1"

def file_search_process(x):
    for r, d, f in os.walk(x):
        if searched_file in f:
            path_container.append(os.path.join(r, searched_file))
            for st in path_container:
                new_string = st.replace("\\", "/")
                choice_list.append(new_string)

            for i in range(len(choice_list)):
                choice_list_dict[i] = choice_list[i] 


def open_read_file(x):
    file_target = open(x, 'r')
    content_container = file_target.readlines()
    for line in content_container:
        print(line.strip())


def root_paths(i):
    for i in available_drives:
        file_search_process(i)

while step == "1":
    try:
        searched_file = input("\n\n\nTyp the file name with file extention, that you're searching for: ")
        print("\nRooting...\n")
        root_paths(available_drives)
        if choice_list_dict:
            step = "2"
        if not choice_list_dict:
            print("\n!!!No such file found!!!\n\nPlease try again.")

        while step == "2":
            try:
                pp.pprint(choice_list_dict, indent=4)
                users_file_choice = int(input("\nChoose a number from above: "))
                if users_file_choice in choice_list_dict.keys():
                    print("\nPls wait for the reading process...\n")
                    open_read_file(choice_list_dict[users_file_choice])
                    print("\n\nReading process: Done!\n\n")
                    step = input("Type 1 to keep searching,\nType 2 to select another file to read,\nPress enter to exit: ")
            except ValueError:
                print("\n"* 10 + "!!!Please use a numeral value in range!!!\n")
    except KeyboardInterrupt:
        exit()   
