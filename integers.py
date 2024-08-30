# integers are numbers without decimal points(either + or -)
# floats have decimal points
# integers are used for arithmetics(math) & work with arithmetic operators(+,-,%,*)
# doubles are variables with a very large decimal number
# methods:
# round(), int(), float()
# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
import math

temp = 56.8926 
temp = round(temp)
print(temp)

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89
temp = 56.8926 
temp = round(temp, 2)
print(temp)

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893 
temp = 56.8926
temp = round(temp, 3)
print(temp)

# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
temp=56.8926
temp = temp * 10
temp = str(temp).replace("56","")
print(temp)