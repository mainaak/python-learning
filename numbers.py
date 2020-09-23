from math import floor as f, ceil as c, sqrt

myNum = -44
myNumStr = str(myNum)
print("This is a string number " + myNumStr)
# print("This is a non string number " + myNum)

print("Absolute:\t" + str(abs(myNum)))
print("Power:\t\t" + str(pow(myNum, 2)))
print("Max:\t\t" + str(max(1, 3, 5, 6)))
print("Round\t\t" + str(round(4.49)))
print("Floor\t\t" + str(f(4.99)))
print("Ceil\t\t" + str(c(4.01)))
print("Sqrt\t\t" + str(sqrt(144)))

inNumber = input("Enter a number\n")
print("The number you entered is " + str(inNumber))
