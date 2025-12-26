# def calculate():
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     op = input("Enter 1 for addition, 2 for subtraction, 3 for divison, 4 for multiplication")

#     if op == "1":
#         print(f"{num1} + {num2} = {num1 + num2}")
#     elif op == "2":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     elif op == "3":
#         print(f"{num1} / {num2} = {num1 / num2}")
#     elif op == "4":
#         print(f"{num1} x {num2} = {num1 * num2}")
#     else:
#         print("Invalid operator")


# while True:
#     calculate()
#     doAgain = input("Do you want to continue (yes/no)?")
#     if doAgain != "yes":
#         break

# def generateTable():
#     num = int(input("Enter a number: "))

#     i = 1
#     while i <= 10:
#         print(f"{num} x {i} = {num*i}")
#         i=i+1

# generateTable()


# for i in range(5): # 0 , 4 with 1 inc
#     print(f"The value is {i}")


# for i in range(2, 5): # 2 , 4 with 1 inc
#     print(f"The value is {i}")

# for i in range(3, 31, 3): # 3 , 30 with 3 inc
#     print(f"The value is {i}")


# for i in range(30, 2, -3): # 30 , 3 with 3 dec
#     print(f"The value is {i}")


# batchCode = "2306B1"

# for a in batchCode:
#     print(a)

students = ["Razan", "Zaeema", "Muheet", "Anas", "Usman", "Saad", "Hamza"]

for std in students:
    print(f"The name is {std}")


