# string is immutable

"""  // same as tuple
CRUD Operations
CREATE => Not Possible -> AttributeError (append, insert, extend) 
READ =>  Possible -> index, count
UPDATE => Not Possible -> TypeError (item assignment)
DELETE => Not Possible -> AttributeError (pop, clear, remove) or typeError (del keyword)
"""


"""
# HELLO 

NEGATIVE_INDEX     POSITIVE_INDEX      CHAR
    -5                   0               H
    -4                   1               E
    -3                   2               L
    -2                   3               L
    -1                   4               O
    
"""

text = "Python Programming"

print(len(text))
print(type(text))
# print(float(text))  #  Error : could not convert string to float

print(text[1])  # print(text[start: stop: step])

t = "1.2"
print(float(t)) # if stored value is float then it works

# Empty String

# t1 = "" or '' or """""" or ''''''
# t1 = " " or '' or """""" or ''''''
# t1 = "" or '5' or """""" or ''''''
t1 = '''"'''

print(len(t1))

print(bool(t1))
print(bool(len(t1)))

# take input and check that string is palindrome or not

# word = input("Enter your word: ")
# if word == word[::-1]:
#     print("It is palindrome")
# else:
#     print("It is not palindrome")


# string concatination and replication

print("Hello" + "World" + "7") # concatination
print("Hello" +  "" + "World" + "7") # concatination  // there is no space
print("Hello" +  " " + "World" + "7") # concatination // there is space 

print("hello" * 5)  # replication # output => hellohellohellohellohello
print("hello * hi") # output => hello* hi   

# movie_name = "Dhurandhar"
# search_text = input("Search movie name: ")


# if search_text in movie_name:
#     print("Movie Found:", movie_name)

# else:
#    print("not found")


"""
String methods => never modifies original string

str_name.method_name()

1. lower() => converts every char from upper to lower
2. upper() => converts every char from lower to upper
3. capitalize() => only converts lower to upper of index 0 and rest will lower case
4. title() = > converts first char of every word to upper and rest will be in lower
5. swapcase() => upper case char to lower and vice versa
6. startswith(val) => True if string starts with given value
7. endswith(val) => True if string ends with given value
8. index(val) => gives index of given value if present otherwise ValueError
9. find(val) => gives index of given value if present otherwise '-1'
10. replace(old, new) => replaces old with new
11. count(value) => provides count of given value
12. script(char = " ") => removes/trims empty spaces from left and right
12. lstrip(char = " ") => removes/trims empty spaces from any left
13. rstrip(char = " ") => removes/trims empty spaces from any right
14. split(sep = " ") => splits/breaks string into list

"""

# index(str, start=0, end=len(str)) -> int

text1 = "pyhton programming in"

# print(text1.index()) # TypeError: index expected at least 1 argument, got 0
print(text1.index("p", 4, 8)) 
print(text1.index("in", 16)) 
# print(text1.index("python", 16))  # ValueError: substring not found

print(text1.find("ll", 16))  # output -> -1 because (ll) is not in text1


text2 = "I like java"

print(text2.count("like")) # output -> 1
print(text2.count("a", 8, 10)) # output -> 1

print(text2.replace("a", "@"))  # output -> I like j@v@
print(text2.replace("a", "@", 1))  # output -> I like j@va
print(text2.replace("a", "@", -1))  # output -> I like j@v@ (default vaalue = -1)


# strip(chars =" ") => removes left and right side spaces 
# lstrip(chars =" ") => removes only left side spaces 
# rstrip(chars =" ") => removes only right side spaces 


text3 = "     hello world    "
print(text3)
print(text3.strip(""), "bye") # (bye) uses to check spaces remove or not  # output -> hello world bye


print(text3.lstrip(), "bye")  # output-> hello world      bye


print(text3.rstrip(), "bye")  # output->      hello world bye


text4 = "    !#@ hello world !   "

# it only romve near value of inverted commas
print(text4.strip("!"), "bye")  # output=>     !#@ hello world !    bye

# in this space is also added so both removed
print(text4.strip("! "), "bye")  # output -> #@ hello world bye

print(text4.strip("!  @#"), "bye") # output -> hello world bye

 
# split(sep=" ", maxsplit= -1) -> list => breaks string to list

r = "hello how are you how 1"

print(r.split()) # output -> ['hello', 'how', 'are', 'you', 'how', '1']

print(r.split("how")) # output -> ['hello ', ' are you ', ' 1']   (default value = -1 means infinte)

print(r.split("how", 1)) # output -> ['hello ', ' are you how 1']


items = ["mango", "pencil", "table"]

print("".join(items)) # output => mangopenciltable


# count number of letter present in given string excluding spaces

text5 = "python programming"

total_len = len(text5)
total_spaces = text5.count(" ")
total_letters = total_len - total_spaces
print(total_letters)

words = text5.split()
print(len("".join(words)))


