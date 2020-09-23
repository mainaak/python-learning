
# different file modes are r(read), w(write), a(append), r+(read & write)
# car_file = open("cars.txt", "r")
# readable(), read(), readline(), readlines()
def read_way_1():
    car_file = open("cars.txt", "r")
    for entry in car_file:
        print(entry)
    car_file.close()


def read_way_2():
    car_file = open("cars.txt", "r")
    list_of_lines = car_file.readlines()
    for entry in range(len(list_of_lines)):
        print(list_of_lines[entry])
    car_file.close()


def write_to_file_1():
    car_file = open("cars.txt", "a")
    car_file.write("\nAlpha Romeo - Kimmi Raikkonen")
    car_file.close()


def copy_file_to_json():
    file_original = open("cars.txt", "r")
    file_copy = open("cars_copy.txt", "w")
    file_copy.write("{")
    key = "1"
    for item in file_original.readlines():
        file_copy.write('"' + key + '": "' + item + '",\n')
        key = str(int(key) + 1)
    file_copy.write("}")
