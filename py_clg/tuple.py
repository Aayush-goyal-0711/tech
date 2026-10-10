# tuple is immutable data type in python

[1, 2, 3] # list
(1, 2, 3) # tuple

t = (1, ("hello",), 3) # if tuple contains only one element then we have to put comma after that element otherwise it will be considered as normal data type.

print(t[1][0]) # output --> hello
print(t) # output --> (1, ('hello',), 3)
print(type(t)) # output --> <class 'tuple'>
print(t[1:]) # output --> (('hello',), 3)  # print(t[start:end:step])  # start is inclusive and end is exclusive

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
   #    0  1  2  3  4  5  6  7  8   9
print(nums[2:7]) # output --> (3, 4, 5, 6, 7) // start default value = 0, end default is lenght of that list/tuple (len(nums)) and, step default value = 1
print(nums[2:7:2]) # output --> (3, 5, 7)

print(nums[::-1]) # output --> (10, 9, 8, 7, 6, 5, 4, 3, 2, 1) // reverse the tuple
print(nums[3:8:-1]) # output --> () // empty tuple because step is negative and start < end

# CREATE(apppend, insert, extend, remove, pop, clear, reverse, sort) => list is mutable data type in python
i = (1, 2, 3)
# i.append(4) // output --> AttributeError: 'tuple' object has no attribute 'append'  # because tuple is immutable data type

# UPDATE => tuple is immutable data type in python
# i[1] = "two" # output --> TypeError: 'tuple' object does not support item assignment  # because tuple is immutable data type

# DELETE => tuple is immutable data type in python
# del i[1] # output --> TypeError: 'tuple' object doesn't support item deletion

# i.pop() # output --> AttributeError: 'tuple' object has no attribute 'pop'  # because tuple is immutable data type
# i.clear() # output --> AttributeError: 'tuple' object has no attribute 'clear'  # because tuple is immutable data type
# i.remove(2) # output --> AttributeError: 'tuple' object has no attribute 'remove'  # because tuple is immutable data type


# COUNT(value => int
j = (1, 2, 3, 2, 4)
print(j.count(2)) # output --> 2  # because 2 is present 2 times in tuple j

# index value => int
print(j.index(2)) # output --> 1  # because 2 is present at index 1 in tuple j

# j.index(value, start, end) # value => int, start => int, end => int
print(j.index(2, 2, 4)) # output --> 3  # because 2 is present at index 3 in tuple j after index 2

# sort changes original but sorted gives new list with sorted values of original list/tuple

# sort() => AttributeError
l = (3, 6, 2, 1)
# l.sort() # output --> AttributeError: 'tuple' object has no attribute 'sort'  # because tuple is immutable data type
print(sorted(l)) # output --> [1, 2, 3, 6]  # sorted() function will return a new list with sorted values of tuple l


# sorted(list, key=None, reverse=False) => list
print(tuple(sorted(l, reverse=True))) # output --> (6, 3, 2, 1)  # sorted() function will return a new list with sorted values of tuple l in reverse order and then we are converting that list into tuple using tuple() function


# tuple/list unpacking

r = (1, 2, 3) 
x, y, z = (4, 5, 6) # unpacking tuple into variables
print(x) # output --> 4
print(y) # output --> 5
print(z) # output --> 6
print(x, y, z) # output --> 4 5 6
print(r[0], r[1], r[2]) # output --> 1 2 3   


# str.split(separator=" ") => list split take string and split it into list of strings by separator and return that list of strings

numbers = input("Enter numbers separated by space: ").split() # input() function will take input from user and split() function will split the input string into list of strings

print(numbers) # output --> ['1', '2', '3', '4', '5']  # list of strings  split default value is pace, so it will split the input string into list of strings by space.

p,q,r = 1,2,3
# p,q,r = (1, 2, 3) 
# p  = 1
# q  = 2  
# r  = 3

# s  = (9) it gives output as int because it is not a tuple, it is an int. If you want to create a tuple with one element then you have to put comma after that element otherwise it will be considered as normal data type.
s = (9,)
print(len(s)) # output --> 1  # because s is a tuple with one element, so len() function will return 1


# swapping of values

j = 10
k = 5

temp = j  # 1. temp me j (10) save kiya
j = k     # 2. j me k (5) dala
k = temp  # 3. k me temp (10) dala

print("j =", j)  # Output: j = 5
print("k =", k)  # Output: k = 10