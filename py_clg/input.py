num = input("Enter a number ")
print("after input")
print("User Input Data:",num)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(int(num1) + int(num2))
print(num1 + num2)

len = float(input("Enter value of Length: "))
bre = float(input("Enter value of Breadth: "))
print(len * bre)


price = float(input("Enter the product price: "))
qty = int(input("Enter the number of products: "))
print("Total Price", price*qty)

n1 = 36.68
n2 = 5.02
print(f"{n1*n2:.2f}")

name = "Aniket"
marks = 88

print(name, "scored", marks, "marks.")
st = f"{name} scored {marks} marks."
print(f"{name} scored {marks} marks.")

price = float(input("Enter the product price: "))
qty = int(input("Enter the number of products: "))
discout = float(input("Enter the discount: "))

total_price = price * qty
discount_amount = total_price * discout /100
final_price = total_price - discount_amount
print(final_price)