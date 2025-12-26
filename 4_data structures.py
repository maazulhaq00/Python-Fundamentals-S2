# ------- list : ordered, mutable, indexed, duplicate values can be stored
fruits = ["mango", "watermelon", "guava"]
# print(fruits[1])

# fruits.append("banana")
# print(fruits)

# fruits.insert(2, "apple")
# print(fruits)

# fruits.pop()
# print(fruits)

# fruits.remove("mango")
# print(fruits)

# fruits[0] = "water melon"
# print(fruits)

# for fruit in fruits:
#     print(f"{fruit} is my favourit fruit")

# ------- tuple : ordered, immutable, indexed, duplicate values can be stored
# grades = ("A+", "A", "B", "C", "Fail")

# print(grades[2])
# print(len(grades))

# grades[0] = "A-one" # error
# grades.append("D") # error
# grades.pop()
# print(grades)

student = ("Hamza", 27, "Karachi")

# student_name = student[0]
# student_age = student[1]
# student_city = student[2]

# tuple unpacking
student_name, student_age, student_city = student

print(student_name)
print(student_age)
print(student_city)

# membership operator "in"

print("Hamza" in student)
print("Razan" in student)
print(22 in student)
print("guava" in fruits)

# ------- sets : unordered, unindexed, unique items
courses = {"JS", "Boostrap", "XML/JSON", "JS"}
print(courses)

courses.add("C#")
print(courses)

# courses.remove("Boostrap")
courses.discard("Boostrap")
print(courses)

# courses.remove("Python") #  error
courses.discard("Python") 
print(courses)


for c in courses:
    print(c)

print("JS" in courses)
print("HTML" in courses)

# {'JS', 'C#', 'XML/JSON'}

courses2 = {"HTML", "Python", "Bootstrap", "JS"}

print(courses | courses2) # union
print(courses & courses2) # intersection
print(courses - courses2) # diff
print(courses2 - courses) # diff
print(courses2 ^ courses) # symmetric diff


