print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Check Even or Odd")
print("6. Percentage")
print("7. Exit")

choice = input("Enter your choice (1-7): ")

if choice == '1':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a + b)

elif choice == '2':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a - b)

elif choice == '3':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a * b)

elif choice == '4':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero")

elif choice == '5':
    n = int(input("Enter your number: "))
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

elif choice == '6':
    a = float(input("Enter part: "))
    b = float(input("Enter whole: "))
    if b != 0:
        print("Percentage:", (a / b) * 100, "%")
    else:
        print("Error: Division by zero")

elif choice == '7':
    print("Good Bye")

else:
    print("Invalid Input")