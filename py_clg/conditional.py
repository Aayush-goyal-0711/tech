# you can use if block without else block but you cannot use else block without if block

"""
SYNTAX

if conditions:
    # statements // the space before it is called indentation 
else:
    # statements
"""

if True:
    print("HELLO WORLD")
    print("HELLO WORLD")
print("HELLO WORLD")  # this will not in if statement
print("HELLO WORLD")  # this will not in if statement


t = False 

# condition is True then if block will be executed
# condition is False then else block will be executed
if t:
    print("true")
else:
    print("false")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


if age < 14:
    print("You are a child")
elif age >= 14 and age < 18:
    print("You cannot drive")
elif age >= 18 and age <= 80:
    print("You can drive")
else:
    print("You are too old to drive")


# Match/switch case

name = input("Enter your name: ")

match name:
    case "Raj":
        print("Your Roll no. is 1")
    case "Aayush":
        print("Your Roll no. is 2")
    case "Aniket":
        print("Your Roll no. is 3")
    case "Ravi":
        print("Your Roll no. is 4")
    case _:
        print("Enter a valid name")

age, marks = 16, 75
# if age >= 18:
#     if marks >= 75:
#         print("You are eligible for scholarship")
#     else:
#         print("You are not eligible for scholarship")
# else:
#     print("You are not eligible for scholarship")


if age >= 18 and marks >= 75:
    print("You are eligible for scholarship")
else:
    print("You are not eligible for scholarship")