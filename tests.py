# print all letters except 'e' and 's'
i = 0
a = 'GeeksforGeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
       i += 1
       continue

    print(f"Current letter: {a[i]}")
    i += 1
     
# password checker:
attempts = 3

# trial 1
password = str(input("Enter password: "))
username = str(input("Enter username: "))
if password == 'secret123' and username == 'admin':
    print(f"Access to {username} is granted")
elif password != 'secret123' and username == 'admin':
    attempts -= 1
    print(f"Attempts left: {attempts}") 

# trial 2
password = str(input("Enter password: "))
username = str(input("Enter username: "))
if password == 'secret123' and username == 'admin':
    print(f"Access granted to {username}")    
elif password != 'secret123' and username == 'admin':
    attempts -= 1
    print(f"Attempts left: {attempts}") 
                          
# trial 3
password = str(input("Enter password: "))
username = str(input("Enter username: "))
if password == 'secret123' and username == 'admin':
    print(f"Access granted to {username}")    
elif password != 'secret123' and username == 'admin':
    attempts -= 1
    print(f"Attempts left: {attempts}")

# block account
if attempts == 0 and password != 'secret123' and username == 'admin':
    print(f"Access denied !! The account {username} has been blocked ! check in after 24 hours") 

# bouncing ball problem:
initial_height = 10
bouncing_factor = 0.5
height = initial_height
while height > 0.1:
    print(f"the ball is bouncing at a height of {height}")
    height *= bouncing_factor 
print("The ball has stopped bouncing")    

# 