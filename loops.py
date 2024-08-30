# for loop
# print numbers 1 to 50 in a list:
# range() function creates the numbers
ls1 = [x for x in range(1,51)]
print(ls1)

# iterating over a list of strings:
# enumerate() enables the list elements to have their own index
ls2 = ["me","you","them","we","us"]
for count, ele in enumerate(ls2):
    print(count, ele)

# dictionary iteration:
# creating an empty dictionary:
d = dict()

# creating key-value pairs in the dictionary:
d['abc'] = 123
d['def'] = 456

# iterating over the key-value pairs:
for i in d:
    print("% s % d" % (i, d[i]))

# for loop with tuples:
t = ((1,2),(3,4),(5,6),(6,7))
for a, b in t:
    print(a, b)

# looping through parallel lists:
fruits = ["Apple","Banana","Orange","Carrot"]
colors = ["Red","Yellow","Orange","Orange"]

# looping through both:
for fruit, color in zip(fruits, colors):
    print(f"fruit: {fruit} is {color}")

#control structures:
# continue
# do not output s or e:
# continue iterates over an element
for letters in 'geeks for geeks':
    if letters == 'e' or letters == 's':
       continue
    print(letters)
 
# break
# break - breaks a loop making it stop 
for letters in 'geeks for geeks':
    if letters == 'e' or letters == 'g':
         break
    print("Current letter:",letters)
    
# pass statement
# used to create an empty loop, also used in function and classes
for letters in 'geeks for geeks':
    pass
print("last letter:",letters)

# for - else loop:
for i in range(1, 20, 2):
    print(i)
else: #executed because there is no break statement:
    print("No Break\n")

# exercise:
# code to implement continue statement:
clothes = ["Jacket","Shirt","Socks","Trousers","Vests"] 
pairedSocks = []
for item in clothes:
    if item == 'socks':
        continue
    else:
        print(f"washing {item}")
pairedSocks.append("socks")
print(f"washing {pairedSocks}")           

# code to implement range function in for loop:
for day in range(1,8):
    distance = 3 + (day - 1) * 0.5
    print(f"Day {day}:Run Distance {distance} miles")
    
#calculating probability:
# a bag of 20 marbles, 4 are blue, what are the chances i'll pick 4 blue marbles
def probability():
   f = int(input("Number of possible outcomes: "))
   N = int(input("Number of all outcomes: "))
   classicalProbability = f/N
   print(f"probability: {classicalProbability}")
probability()   

# initializing counter value to zero:
counter = 0

# creating a loop for counter:

while True:
    # incrementing the counter value by 1 for each loop:
    counter += 1
    # outputting the counter value:
    print(f"count: {counter}")
# checking for a condition to stop the loop:
    if counter == 20:
        # using break statement to stop the loop:
        break
#output after loop stops:
print("loop has ended!")    


x = [i for i in range(1,1001)]

for i in x:
    if i >= 20 and i <= 500 and i % 2 == 0:
     print(i)