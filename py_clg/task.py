"""
Q1. Write a program that takes a number and prints:

* Positive if > 0
* Negative if < 0
* Zero if = 0
"""
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


    
# Q2. Take two numbers as input and print the larger number.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} and {b} are equal")



# Q3. Largest of Three

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

if x >= y and x >= z:
    print(f"{x} is the largest number")
elif y >= x and y >= z:
    print(f"{y} is the largest number")
else:
    print(f"{z} is the largest number")



# Q4. Take a number as input and print whether it is even or odd.

n = int(input("Enter a number: "))

if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")

    
    
# Q5. Take a number(year) as input and print whether it is leap year or not.

year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")