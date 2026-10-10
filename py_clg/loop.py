numbers = [1, 2, 3, 4, 5]

# for value in numbers:
    # print(value)
    # print(value * 0.3 + value)


# 1) if we provide a single value to range function then that value is for stop.
# 2) if we providing multiple value to range function then there order will be start stop and step.
# 3) stop value is required.
# 4) if start and stop value are same then loop while not execute.
# 5) range data type is range.
# 6) step default value is 1.
# 7) start default value is 0.


# range(stop)
# range(start, stop)
# range(start, stop, step)

# for num in range(5):
#     print(num)

# for num1 in range(1,101):
#     print(num1)

# for num2 in range(1,101,2):
#     print(num2)

# for num3 in range(5,101,5):
#     print(num3)

mrks = [47, 30, 67, 29, 88, 56, 20]

maximum = mrks[0]
for m in mrks:
    if m > maximum:
        maximum = m

print(maximum)

book_prices = [159, 99, 499, 199, 2499]

# print(sum(book_prices)) //1//// this is not write way to written in exam

total_price = 0
discount = 10
for price in book_prices:
    if price > 199:
        total_price = total_price + price - 0.1 * price
    else:
        total_price = total_price + price

print(total_price)


num4 = [159, 99, 499, 199, 2499]

count = 0

for num in num4:
    if num > 199:
        count = count + 1
        
print(count)




item = input("Item name: ")
qty = int(input("Quantity: "))
price = float(input("Price per item: "))

print(f"{qty} x {item} at {price:.2f} each")
print(f"Total payable: {qty * price:.2f}")
