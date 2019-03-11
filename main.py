def add(num1, num2):
    """Returns num1 plus num2.  One stop programming is cool"""
    return num1 + num2

def sub(num1, num2):
    """Returns num1 plus num2.  One stop programming is cool"""
    return num1 - num2

def mul(num1, num2):
    """Returns num1 plus num2.  One stop programming is cool"""
    return num1 * num2

def div(num1, num2):
    """Returns num1 plus num2.  One stop programming is cool"""
    return num1 / num2


def main():
    num1 = int(input("What is your 1?"))
    num2 = int(input("What is your 2?"))
    operation = int(input("What do you want to do? 1. add, 2. subtract, 3. multiply, or 4. divide. Enter number: "))
    if(operation == 1):
        print("Adding...")
        print(add(num1, num2))
    elif(operation == 2):
        print("Subtracting...")
        print(sub(num1, num2))
    elif(operation == 3):
        print("Multiplying...")
        print(mul(num1, num2))
    elif (operation == 4):
        print("dividing...")
        print(div(num1, num2))
    else:
        print("I don't understand")

main()
