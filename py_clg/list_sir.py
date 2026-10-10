nums = [1,2,3,4,5]
# -len(nums)
# -len(nums) + 1
# -len(nums) + 2
# -len(nums) + 3

a = []
# b = ["Aniket", 20, True, 2 + 3j, [1,3, [6,3,[]]], [2,5], 3.14]

# print("Type:",type(nums))
# print("Length:", len(nums))

start_index = 0 or -len(nums)
last_index = len(nums) - 1  or -1

"""
CRUD operations
C - CREATE
R - READ
U - UPDATE
D - DELETE
"""

#READ
# n = [3,1,4,["Aniket",["Noida"], True]]
# print(n[3][1][0])
# x = [3,1,4,["Aniket",["Noida"], True],["hello"]]
# print(x[4][0])

#CREATE
"""
List Methods for create (modifies original list)
1. append(value) -> None => Inserts value at end
2. insert(index, value) -> None => Inserts value at given index
3. extend([multiple values]) -> None => Inserts multiple values at end
"""
names = ["Aniket", "Himanshu", "Gulshan"]

names.append("Chirag")
names.append("Anish")
# names.append(1,2) #WRONG
# names.append([1,2])
# names.extend([1,2,3,4,5])
names.insert(2,"New Data")
# print("Appended",names)
# print("Inserted",names)

# UPDATE

# x = [ "one", "two",[3, 4], "three"]
# x[2][0] = "new value"
# print(x)

# DELETE/REMOVE

# del keyword => deletes value at given index
# pop(index = -1) -> deleted value => list method => deletes value at given index
# remove(value) -> None =>  list method => deletes first matched value

n = [1,2,1,1,3,4,2,5]

# print("before remove",n)
# del n[4]
# print("deleted value:",n.pop(4))
# n.remove(2)
# print("after remove",n)

# INDEX => list method

# index(value,start = 0,stop=len(list)) ->int
# index of first matched value

# m = ["hello", "hi", "bye","hi"]

# index_of_value = m.index("hi",2,3)
# print("Index:", index_of_value)

c = [1,2,[3,4]]

# idx = c.index([3,4])
# print((c[idx].index(3)))


var = [[1,3,4]]
# idx = c.index(var[0])
# print((c[idx].index(3)))

"""
you have a list containing multiple list.
Find the index of value that is 5 which is present inside first list.
"""

p = [[1,3,5,2], [3,1,2,5] , [5,2,1,3]]

# print(p[1].index(5))

# Membership Operator ('in' and 'not in') -> bool
# works on sequence/iterable(str,list,tuple) type of data

# text = "hello, how are you?"

# j = [1, 2, 345, [4,5],"hello"]

# print( "o" in j[-1])

# Reverse => list method => list_name.reverse() -> None
# j.reverse()
# print(j)


# Sorting
"""
1. sort(reverse=False, key=None) -> None => list method => sorts list in asc order by default
2. sorted(list_name, reverse=False, key=None) -> List => direct built methods => sorts list in asc order by default and provides new list in return without changing orignal list.
"""

nums = [7,4,6,8,10,9,1,5,3,2]

# nums.sort() # asc
nums.sort(reverse=True) # dsc
# nums.reverse() # same as reverse = True
# print(nums)


# x = [1,2,3,"hello"]
# x.sort()
# print(x)


# y = ["xyz", "pqr", "klm","kmn"]
# y = ["a", "j", "X", "b", "Z"]
# y.sort()
# print(y)


# v = ["aditya", "adi9tya"]
# v.sort()
# print(v)

# g = [1,True, False,0 , -1]
# g.sort()
# print(g)

k = ["himanshu", "gulshan", "chirag", "aniket","Abhimanyu"]

# [8, 7, 6, 6, 9]
# [6, 6 ,7 , 8, 9]
# ["aniket", "chirag", "gulshan", "himanshu", "abhimanyu"]
k.sort(key=len)
# print(k)

t = ["v", "H", "d", "a", "Z"]
t.sort(key=str.lower)
# ["v", "h","d","a","z"]
# ["a","d","h","v","z"]
# ["a","d","H","v","Z"]
# print(t)


l = [0,1,2,3,-4,4,7,6,5,8,9,10]

def hello(num):
    print(num , num % 2 == 0 and num + 1)
    return num % 2 == 0 and num + 1

l.sort(key=hello)
# l.sort(key=hello)

# [1,False, 3, False,-3, 5, False, 7, False, 9 , False, 11]
# [1, 0, 3, 0, -3, 5, 0, 7, 0, 9, 0, 11]
# [-3,0,0,0,0,0,1,3,5,7,9,11]
# [-4,0,1,3,5,7,9,2,4,6,8,10]
print(l)
# print(l)

# print(sorted(l,reverse=False,key=hello))



"""
Direct Built In methods
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
# min(list_name) -> value_type

o = [45, 65, 28, 99, 163, 2, 57]
# print("MAXIMUM",max(o))
# print("MINIMUM",min(o))

k =[True , False, 2,-5.3, 3.64]
# print(max(k))
# print(min(k))

l = ["h5ye","h8ii","h9ello"]

# print(max(l))

#sum(list_name,start=0) -> int

# i = ["hello", "hii", "bye"]
# i = ["1", "2", "3"]
# i = [True , False, 65]

# i = [1.2,1,3]
# start = True
# start = 1
# start = start + i[0]
# start = start + i[1]
# start = start + i[2]

# print(sum(i,start=True))


# clear() -> None => modifies original list and removes everything
# v = [1,2,3,4,5]
# v.clear()
# print(v)

# copy() -> list => list method that copies only value of object not address/reference

u = [1,2,3]
# v = u
v = u.copy()
v.append(4)
u.pop(1)
print("U", u)
print("V", v)