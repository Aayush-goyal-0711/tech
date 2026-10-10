# Stings are immutable

"""
CRUD Operations

CREATE => Not Possible => AtrributeError (append,insert,extend)
READ => Possible
UPDATE => Not Possible => TypeError
DELETE => Not Possible => AtrributeError(pop,remove,clear) or TypeError (del keyword)
"""


"""
# Hello
Negative_INDEX    Postive_INDEX     CHAR
-5                0                 H
-4                1                 e
-3                2                 l
-2                3                 l
-1                4                 o                 
"""

text = "Python Programming"
# print(text[::-1])
# print(len(text))
# print(type(text))
# print(text[0])
# print(text[1])
# print(text[2])
# print(text[3])
# print(text[4])
# print(text[5])

# Empty String
t = "" or '' or """""" or ''''''

# print(len(t))
# print(bool(t))
# print(bool(len(t)))


# take input and check that string is palindrome or not

# word = input("Enter your word: ")
# if word == word[::-1]:
#     print("It is Palindrome")
# else:    
#     print("It is not Palindrome")


# string concatination and replication

# print("hello"+ " " * 5 + "world") # "hello" + "     " + "world"
# print("hello " * 5)

# "hello" + "hello" + "hello" + "hello" + "hello"
# "hellohellohellohellohello"

# print("lo w" in "hello world")
# print("h" not in "hello")

# movie_name = "Dhurandhar"
# search_text = input("Search movie name: ")

# if search_text in movie_name:
#     print("Movie found:", movie_name)
# else:
#     print("not found")


"""
String methods => never modifies original string

str_name.method_name()

1. lower() => converts every char from upper to lower

2. upper() => converts every char from lower to upper

3. capitalize() => only converts lower to upper of index 0 and rest into lower

4. title() => converts first char of every word to upper and rest will be in lower

5. swapcase() => uppercase char to lower and vice versa

6. startswith(val) => True if string starts with given value

7. endswith(val) => True if string ends with given value

8. index(val) => gives index of given value if present otherwise ValueError

9. find(val) => gives index of given value if present otherwise '-1'

10. replace(old,new) => replaces old with new

11. count(value) => provides count of given value

12. strip(char = " ") => removes/trims empty spaces from left and right

13. lstrip(char = " ") => removes/trims empty spaces from ony left

14. rstrip(char = " ") => removes/trims empty spaces from ony right

15. split(sep=" ",maxsplit="-1") => splits/breaks string into list

16. join(list) => merges/joins list values into string

17. isalpha() => True if string has only alphabets

18. isdigit() => True if string has only numbers

19. isalnum() => True if string has both alphabets and nums

20. isspace() => True if string has only spaces

21. islower() => True if all chars are in lowercase
22. isupper() => True if all chars are in uppercase
23. iscapitalize() => True if only index 0 char is upper and rest in lower
24. istitle() => True if all words first char is in upper and rest in lower
"""

q = "hELlo hOw arE You?"
# print("OG:",q)
# print("LOWER:",q.lower())
# print("UPPER:",q.upper())
# print("CAPITALIZE:",q.capitalize())
# print("TITLE:",q.title())
# print("SWAPCASE:",q.swapcase())

# print("ISLOWER:", "hello".islower())
# print("ISLOWER:", "HELLO".swapcase().islower())

q2 = "python programming"

#yth
# print(q2.startswith(("yth","z"),1,4))
# print(q2.endswith("ing",1,4))


# print("testing".startswith(("test", "t", "T", "Test")))

"""
A shop records the following information:
item = "Laptop"
price = 45000
quantity = 2
discount = 10

Write Python statements to:
Calculate the total price before discount.
Calculate the discount amount and final payable amount.
Display the final amount along with its data type.
Modify the program so that the quantity is taken from the user instead of being fixed as 2.
"""

# index(str,start=0,end=len(str)) -> int

# text1 = "python programming in"

# print(text1.index("in",16))
# print(text1.find("python"))

text2 = "I like java"
# print(text2.count("a",8,10))
# print(text2.replace("a","@",1))


# strip(chars=" ") => removes left and right side spaces
# lstrip(chars=" ") => removes only left side spaces
# rstrip(chars=" ") => removes only right side spaces

# text6 = "!  #@    !!!####hello world!!    "
# print(text6,"bye")
# print(text6.strip("!# "),"bye")
# print(text6.lstrip(),"bye")
# print(text6.rstrip(),"bye")

# split(sep=" ",maxsplit=-1) -> list => breaks string to list

r = "hello how are you how 1"
# r = "1-2-3"
# r = "1&3"

# print(r.split("how",50))

# items = ["mango", "pencil", "table"]

# print("".join(items))

# count number of letter present in given string excluding spaces

text9 = "Python Programming"

# total_len = len(text9)
# total_spaces = text9.count(" ")
# total_letters = total_len - total_spaces
# print(total_letters)

words = text9.split()
print(len("".join(words)))