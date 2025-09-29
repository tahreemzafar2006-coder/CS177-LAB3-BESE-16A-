def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def percentage(a, b):
    return (a / b) * 100

oppp = int(input("How many times do you want to run the program? "))

for op in range(oppp):
    idea = int(input("Press 0 for Arithmetic operation:\n1 for Checking Even/Odd:\n2 for Percentage:\n"))

    # ✅ If idea is invalid, skip everything
    if idea not in [0, 1, 2]:
        print("Invalid Input")
        continue  

    repetition = int(input("How many times do you want to perform this operation? "))

    if idea == 0:  # Arithmetic
        for i in range(repetition):
            num1 = int(input("Enter your first number: "))
            operation = input("Enter your operation (+, -, *, /): ")
            num2 = int(input("Enter your second number: "))

            if operation == "+":
                print("Your result is:", add(num1, num2))
            elif operation == "-":
                print("Your result is:", subtract(num1, num2))
            elif operation == "*":
                print("Your result is:", multiplication(num1, num2))
            elif operation == "/":
                if num2 == 0:
                    print("Error: Division by zero!")
                else:
                    print("Your result is:", division(num1, num2))
            else:
                print("Invalid operation!!")

    elif idea == 1:  # Even/Odd
        for i in range(repetition):
            num3 = int(input("Enter your number: "))
            if num3 == 0:
                print("Your entered number is zero")
            elif num3 % 2 == 0:
                print("Your number is even")
            else:
                print("It is odd")

    elif idea == 2:  # Percentage
        for i in range(repetition):
            a = int(input("Enter your obtained marks: "))
            b = int(input("Enter your total marks: "))
            if b == 0:
                print("Error: Total marks cannot be zero!")
            else:
                print("Your percentage is:", percentage(a, b))
