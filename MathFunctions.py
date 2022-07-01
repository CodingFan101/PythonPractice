def accumulator_with_for(number):
    total = 0
    for i in range(number):
        total += i
    return total

def remainder(integer):
    if (integer % 2 == 0):
        print("Your number of choice is even.")
    else:
        print("Your number of choice is odd.")

choice = int(input("Insert a number to add all the positive numbers up to: "))
result = accumulator_with_for(choice)
print(result)

decision = int(input("Insert a number to know if it's odd or even: "))
remainder(decision)