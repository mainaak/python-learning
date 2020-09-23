def exception_handling():
    try:
        num = int(input("Enter a numerator:\n"))
        den = int(input("Enter a denominator:\n"))
        print("Result is: " + str(num/den))
        return 1
    except ZeroDivisionError as err:
        print(err)
        print("You cannot divide a number by 0")
        return 0
    except ValueError:
        print("Please only enter numbers")
        return 0


loop_variable = 0
while loop_variable == 0:
    loop_variable = exception_handling()


