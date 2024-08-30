# we loop through a dictionary using the key - value pairs:
person ={
    'name' : "Rick",
    'age' : 20,
    'city' : "Nairobi",
    'location' : "Corner hse",
    'email' : "wabalabadubdub@gmail.com"
}

# use inbuilt zip() function to loop through 2 or more dictionaries, lists
# looping through person
for key, value in person.items():
    print(key,value)

#looping through keys only
for key in person.keys():
    print(key)

#looping through values only
for value in person.values():
    print(value)  

# to loop through 2 dictionaries at the same time:
player = {
    'id':100,
    'username':"Ninja101.",
    'character':"Kelly"    
}
playerDeets = {
    'email':"someone@gmail.com",
    'payment info':True,
    'Date Of Birth':'20-01-2000'
}
# using zip() function 
for (a,b),(a1,b1) in zip(player.items(),playerDeets.items()):
    print(a,b)
    print(a1,b1)