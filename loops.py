my_list = ["Some", "Random", "Piece", "Of", "Information", "Here", 1, 3, 4, 2]


def while_loop():
    counter = 0
    while counter < len(my_list):
        if str(my_list[counter]).endswith("e"):
            print(my_list[counter])
        counter += 1


def for_loops():
    for word in my_list:
        for alphabet in str(word):
            print(alphabet)


# you can also use range with two parameters if you want to pick an index to start it from
def for_loop_range(count_of_execution, list_name):
    for i in range(count_of_execution):
        print(str(list_name[i]))


for_loop_range(len(my_list), my_list)

