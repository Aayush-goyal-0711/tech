[1, 2, 3] # List
(1, 2, 3) # Tuple


t = ( 1, ("Hello", True), 3)
# print(t[0:2:2])


# slicing -> list/tuple/str

# start:stop:step
# 0:length:1


nums = [1,2,3,4,5,6,7,8,9,10]

# print(nums[:]) # without start (0) and stop (len(nums))
# print(nums[3:]) # without stop (len(nums))
# print(nums[:6]) # without start (0)

# print(nums[::]) # without start (0), stop (length) and step (1)
# print(nums[::4]) # without start (0) and stop (length)
# print(nums[3::4]) # without stop (length)
# print(nums[3:8:2]) # with start, stop and step

# print(nums[::-1])
print(nums[7:2:-2])
# print(nums[7:2:-2])

# CREATE (append,insert,extend) => AtrributeError
i = ( 1,2,3 )
# i.extend([4])

# UPDATE => TypeError
# i[1] = "two"

#DELETE => TypeError or AttributeError
# del i[3] # TypeError
# i.pop() # AttributeError
# i.remove(3) # AttributeError
# i.clear() # AttributeError

# count(value) -> int
j = (1,2,3,2,4)
# print(j.count(5))

# index(value,start=0,stop=len(list)) -> int
# print(j.index(2))

# sort() => AttributeError
l = (3,6,2,1)
# l.sort()

# sorted(list,key=None,reverse=False) -> list
# print(tuple(sorted(l)))


# tuple Packing

o = 1,2,3
# (1,2,3)
print("O", o)
print("Type of O:",type(o))

p = (9,)
print("P", p)
print("Type of P:",type(p))
# if len(p) == 1 then add ',' in last


# tuple/list unpacking

x,y,z = ("Aniket", "Aditya", "Rohan")
# print(r[0])
# print(r[1])
# print(r[2])

# str.split(seprator=" ") -> list
# s = input("Enter 4 value: ").split("-")
# print(s)

p,q,r = 1,2,3
# p,q,r = (1,2,3)
# p= 1
# q = 2
# r = 3

s = (9)
print(len(s))

# 1. 1
# 2. 9
# 3. Error
# 4. 0

#swapping of values

j = 10
k = 5
# temp = j
# k = j
# j = temp

j,k = k, j