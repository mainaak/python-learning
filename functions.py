from math import pow
# this contains how to create functions


def ask_number(prompt_message):
    number_fn = input(prompt_message)
    return int(number_fn)


number = ask_number("Please enter a number to cube\n")
print("The cube of the entered number is: " + str(pow(number, 3)))

