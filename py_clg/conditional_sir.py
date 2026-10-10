"""
SYNTAX

if condition:
    #statements
else:
    #statements
"""

# if True:
#     print("vhmfdbfd")
#     print("vhdmsjk")
# print("vhdmsjk")
# print("vhdmsjk")
# print("vhdmsjk")

# t = False
# # condition is True then if block will be executed
# # condition is False then else block will be executed
# if t:
#     print("true")
# else:
#     print("false")

# age = int(input("Enter your age: "))

# if age >=18:
#     print("you can vote")
# else:
#     print("you can't vote")
    

# if age < 14:
#     print("you are a child")
# elif age >= 14 and age < 18:
#     print("You can't drive")
# elif age >=18 and age <= 80:
#     print("You can drive")
# else:
#     print("You are too old to drive")

# match/switch case

# name = input("Enter you name: ")

# match name:
#     case "Raj":
#         print("your roll no. is 1")
#     case "Aniket":
#         print("your roll no. is 2")
#     case "Rahul":
#         print("your roll no. is 3")
#     case "Ravi":
#         print("your roll no. is 4")
#     case _:
#         print("Enter a valid name")

age, marks = 16, 75

# Nested If-Else

# if age >=18:
#     if marks >= 75:
#         print("You are eligible for scholarship")
#     else:
#         print("You are not eligible for scholarship")
# else:
#     print("You are not eligible for scholarship")


# if age >=18 and marks >= 75:
#     print("You are eligible for scholarship")
# else:
#     print("You are not eligible for scholarship")



print("""
    1. Create an user data
    2. Read all users data
    3. Update user data
    4. Delete user
    5. Exit      
""")

choice = int(input("Enter you choice: "))

match choice:
    case 1:
        print("Create an user data")
    case 2:
        print("Read all users data")
    case 3:
        print("Update user data")
    case 4:
        print("Delete user")
    case 5:
        print("Exit")
    case _:
        print("Enter a valid choice")