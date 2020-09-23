# gender = input("What's your gender? (male/female)\n")
# gender = gender.lower()
#
# name: str
# pizza: str
# name = input("What's your name?\n")
# pizza = input("Do you like pizza? (yes/no)\n")
#
# condition_check = pizza.lower() == 'yes' or pizza.lower() == "y"
#
# if gender == 'male':
#     if condition_check:
#         print(name + " likes pizza and is male")
#     else:
#         print(name + " doesn't like pizza and is male")
# elif gender == 'female':
#     if condition_check:
#         print(name + " likes pizza and is female")
#     else:
#         print(name + " doesn't like pizza and is female")


def find_max(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            return n1
        else:
            return n3
    elif n2 > n3:
        return n2
    else:
        return n3


print(find_max(20, 86, 93))
