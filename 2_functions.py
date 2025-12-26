def greet(name):
    print("================")
    print("Hello " + name)
    print("================")

# print("line outside function")

# greet("Ali")
# greet("Razan")
# greet("Hamza")


def calculate():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter 1 for addition, 2 for subtraction, 3 for divison, 4 for multiplication")

    if op == "1":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif op == "2":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif op == "3":
        print(f"{num1} / {num2} = {num1 / num2}")
    elif op == "4":
        print(f"{num1} x {num2} = {num1 * num2}")
    else:
        print("Invalid operator")

calculate()
