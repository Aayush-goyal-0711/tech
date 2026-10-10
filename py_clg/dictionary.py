# collection of multiple different data types stored as an key : value pairs

# key -> value
# values -> can be duplicate 

# dictionary is mutable
# dictionary is unordered

# student_data = ["Aayush", 11, test@test.com]

student_data = {
    "fname" : "Aayush",
    "lname" : "Max",
    10 : "aa",
    (1, 2) : 2,
}
print(student_data)


book = {
    "title" : "Harry Potter",
    "author": "JK Rowling",
    "year"  :  1997
}

# READ

print(book["title"])

# CREATE

book["publisher"] = "ABC"
print(book)

# UPDATE

book["year"] = 2000

# POP



del book["title"]
print(book)

print(book.get("title"))
print(book.get("title", "xyz"))


# empty_dict = {}

# list => dict                /\/ o
# dict = list -> [keys]       \/es


print(book.pop("title"))
print(book.popitem("title"))