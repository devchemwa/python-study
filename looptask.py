# task1
# take input of a user and check if the number is even if not  display odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"number: {num} is even")
else:
    print(f"number: {num} is odd")    

# task2
num1 = int(input("Enter a number: "))
if num1 % 2 != 0:
    print(f"number: {num1} is odd")
else:
    print(f"number: {num1} is even")    

# grading system:
grade = int(input("Enter student marks: "))
if grade >= 0 and grade <= 100:
    if grade > 80:
        print(f"grade: A")
    elif grade > 70 and grade < 80:
        print(f"grade: B")
    elif grade > 60 and grade < 60:
        print(f"grade: C")
    else:
        print(f"grade: D")        
else:
    print("false marks")


# take three numbers from a user and print the greatest of the three:
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a > b and a > c:
    print(f"number: {a} is greater than numbers: {b} and {c}")
elif b > a and b > c:
    print(f"number: {b} is greater than numbers: {a} and {c}")
elif c > a and c > b:
    print(f"number: {c} is greater than numbers: {a} and {b}")
elif a == b and a == c and b == c:
    print("all numbers are equal")
else:
    print("false input: NaN")    

# 3. >>Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
x = int(input("enter a number: "))
y = int(input("enter a number: "))
# checking if x is between 10 and 20:
if x >= 10 and x <= 20 and y > 100:
    print("conditions met")
else:
    print("conditions not met")

# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password = input("Enter your password: ")
if password == "secret123":
    print("Access Granted")
else:
    print("Access Denied")    

# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
student_score = int(input("Enter your score: "))
attendance = int(input("Student attendance: "))
# checking if score is greater than 90:
if student_score >= 90:
    pass
    if attendance >= 80:
        print(f"score: {student_score}. Excellent student") 
    else:
        print(f"score: {student_score} is a good score but attendance: {attendance} needs improvement.")       