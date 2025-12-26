# name="Tabish"
# age=19

# print("My name is " + name + ". I am " + str(age) + " year old." )


# if age<18:
#     print("============================")
#     print("You are not eligible to vote")
#     print("============================")
# elif age==18:
#     print("============================")
#     print("Welcome NEW VOTER !!!!!!!!!!")
#     print("============================")
# else:
#     print("============================")
#     print("You are eligible to vote    ")
#     print("============================")

# task : take a number as user input, check if nuumber is even or odd

num1 = int(input("Enter a number:")) # input & type casting

# if num1 % 2 == 0: 
#     print(f"{num1} is even") # interpolation
# else:
#     print(f"{num1} is odd")

# short hand if-else
print(f"{num1} is even") if num1 % 2 == 0 else print(f"{num1} is odd")