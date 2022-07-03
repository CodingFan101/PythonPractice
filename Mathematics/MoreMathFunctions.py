def addition(x, y):
    sum = x + y
    print("The result of your operation of choice is: " + str(sum))

def subtraction(a, b):
    difference = a - b
    print("The result of your operation of choice is: " + str(difference))

def multiplication(y, z):
    product = y * z
    print("The result of your operation of choice is: " + str(product))

def division(c, d):
    quotient = c / d
    print("The result of your operation of choice is: " + str(quotient))

try:
    number1 = int(input("Insert one number: "))
    number2 = int(input("Insert another number: "))
    operation = input("What would you like to do with these two numbers? ")

    if operation == "Addition" or operation == "addition":
        addition(number1, number2)
    elif operation == "Subtraction" or operation == "subtraction":
        subtraction(number1, number2)
    elif operation == "Multiplication" or operation == "multiplication":
        multiplication(number1, number2)
    elif operation == "Division" or operation == "division":
        division(number1, number2)
    else:
        print("That is not a valid response.")
except ValueError:
    print("You have to type in a number.")
