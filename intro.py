# introduction to python
# variables
# rules of naming variables 
# 1. do not space 
# 2. do not use special characters or numbers to start variable name
# 3. do not use a hyphen
# 4. use lowercase letters (snakecase or camelCase is preferred)
# 5. cannot contain reserved keywords e.g. print
firstName = input("Enter your first name: ")
secondName = input("Enter your second name: ")
# string methods:
# string to uppercase
print(firstName.upper())
# string to lowercase
print(firstName.lower())
# string concatenation
name = firstName + "" + secondName
print(name)
# remove white spaces from both ends
print(name.strip())
# to get the number of characters in a string
print(name.count())
# indexing and slicing strings
var = "John Doe"
print(var[0])
# string splitting
s1 = "The dog was a brown, short German Shephard"
print(s1.split(","))

