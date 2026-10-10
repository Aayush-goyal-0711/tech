# list is mutable data type in python

nums = [1, 2, 3, 4, 5]
    #   0  1  2  3  4  <---- index
    #  -5 -4 -3 -2 -1  <---- index
a = []
b = ["Aayush", 18, True, 2 + 3j, [1,3], [5,7], 3.14] # 2D list because another list is present in parent list
c = ["Aayush", 18, True, 2 + 3j, [1,3, [2,3]], 3.14] # 3D list because another list is present in children 

print("Type:", type(nums))

print("Length:", len(nums))
print("Length:", len(b))
print("Length:", len(c))

start_index = 0 or -len(nums)
last_index = len(nums) - 1 or -1

'''
CRUD Operations
C - CREATE
R - READ
U - UPDATE
D - DELETE
'''

# READ 
n = [3, 1, 4, ["Aayush", True]] # 2D
print(n[-4])
print(n[-1][0]) # output --> Aayush


'''
List Methods for Create
# all three will modify original list
1. list_name.append(value) -> None => Inserts value at end
2. list_name.insert(index, value) ->  None => Inserts value at given index
3. list_name.extend([multiple values]) -> None => Inserts multiple values at end
'''

names = ["Aayush", "Rohit", "Aniket"]

print(names.append("Abhi"))
# names.append(1, 2) # error
names.append([1, 2])
print("Appended", names)

names.extend([1, 2, 3, 4, 5])
print("Appended", names)

names.insert(1, "New Delhi")
print("Appended", names)

print("Inserted", names)


# UPDATE
x = ["one", "two", [3, 4], "three"]
x[1] = 2
# x[2] = "new value" // if we do this full list will change
x[2][0] = "new value"
# x[100] = 99 // output --> out of range 
print(x)


# DELETE / REMOVE

# del keyword => deletes the value at given index
# pop(index = -1) -> value => deletes the value at given index and returns the deleted value, if index is not provided then last value will be deleted and returned
# # remove(value) -> None => deletes the first occurence of given value(first match value will be deleted)

n = [1, 2, 1, 1, 3, 4, 2, 5]

del n[4] # output --> [1, 2, 1, 1, 4, 2, 5]
print(n)

n.pop(2) # output --> [1, 2, 1, 4, 2, 5] 
print(n)

print("deleted value:",n.pop()) # output --> [1, 2, 1, 4, 2] and deleted value: 5
print(n)

n.remove(1) # output --> [2, 1, 4, 2]
print(n)


# INDEX => list_name.index(value) -> index => returns the index of the first occurrence of the value

#  index(value, start = 0, end / stop = len(list_name)) -> index => returns the index of the first occurrence of the value in given range

m = ["Hello","Bye","Hi", "Bye"]

print(m.index("Hi")) # output --> 1
print(m.index("Bye", 2, 4)) # output --> 2

c = [1, 2, 3, [4, 5]]

print(c.index([4, 5])) # output --> 3
idx = c.index([4, 5])
print(c[idx].index(4)) # output --> 0


var = [1, 3, 4]
idx = c.index(var[0])


"""
you have a list containing multiple list. Find the index of value that is 5 which is present inside first list.
"""

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]

print(lst[1].index(5)) # output --> 1


"""
Direct Built In Methods
print()
input()
type()
len()
int()
str()
complex()
abs()
bool()
list()
tuple()
sorted()

max()
min()
sum()
"""

# max(list_name) -> value_type

o = [45, 65, 28, 99, 163, 2, 57]
print("MAXIMUM", max(o))
print(f"MAXIMUM OF {o} is {max(o)}")

print("MINIMUM", min(o))
print(f"MINIMUM OF {o} is {min(o)}")

print(max((True, False))) # output --> True
print(max((True, False, 2))) # output --> 2-
print(max((True, False, 2, -5))) # output --> 2
print(max((True, False, 2, -5, 3.64))) # output --> 3.64

print(min((True, False))) # output --> False
print(min((True, False, 2))) # output --> False
print(min((True, False, 2, -5))) # output --> -5
print(min((True, False, 2, -5, 3.64))) # output --> -5

# l = ["hello", 1]
# print(max(l))  #  not supported between instances of 'int' and 'str'

p = ["hello", "hi", "bye"]
print(max(p))
print(min(p))


p1 = ["hi9", "hidl"]
print(max(p1))

# sum(list_name, start=0) -> int   start default value is 0

# i = ["hello", "hii", "bye"]

# print(sum(i))  # unsupported operand type(s) for +: 'int' and 'str'

i = [1.2, 2,3]
print(sum(i,start=1)) # output --> 7.2

start = True
start = 1
start = start + i[0]
start = start + i[1]
start = start + i[2]

print(sum(i, start = True)) # output --> 7.2


# clear() -> None => modifies the original list and removes all the values from it
v = [1, 2, 3, 4, 5]

print(v)
v.clear()
print(v)


# copy -> list => list method that copies only value of object not address/reference

u = [1, 2, 3]

v = u.copy() # this will copy value after this you can modify u then not affect in v but in v = u it will change

v.append(4)
u.pop(1)
print("U", u)
print("V", v)
