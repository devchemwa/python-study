# how to create a list:
fruits = ["Apple","Banana","Pawpaw","Guava","Avocado"]
print(type(fruits))

# create a list of months, display on terminal:
months = ["January","February","March","April","May","June","July"]
print(months)

# modifying elements in a list:
numbers = [1,2,3,4,5]
numbers[0] = 1
numbers[1] = 2
numbers[3] = 4
numbers[4] = 8
print(numbers)

# accessing elements in a list:
# slicing
fruits = ["Apple","Banana","Pawpaw","Guava","Avocado"]
print(fruits[0])
# to skip some:
print(fruits[0::2])
# to reverse the order:
print(fruits[4::-1])

# list methods:
# .copy()
# fruits.copy() - makes a copy of original list
# .append()
# fruits.append("Loquats") - adds an element to the end of the list
# .pop()
# fruits.pop(3) - removes an element by its index
# .remove
# fruits.remove("Avocado") - removes a target element by specifying it
# .clear()
# fruits.clear() - removes all items in the list