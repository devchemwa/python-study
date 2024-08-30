# take var num and check if positive and divisible by both 2 and 3
        # num = float(input("Enter a number: "))

        # if num > 0:
        #     if num % 2 == 0:
        #         print(f"number: {num} is divisible by 2")
        #         if num % 3 == 0:
        #             print(f"number: {num} is divisible by 3")
        #         else:
        #             pass
        #     else:
        #         pass
        # else:
        #     print("input another number!")


# program to check username and password for login
        # username = input("Enter username: ")
        # password = input("Enter password: ")

        # if password == 'passwaad' and username == 'ninja101':
        #     print(f"User: {username}. Login Success")
        # else:
        #     print(f"User: {username}. Login Failed!")    
            
        # # check if num is a palindrome
        # number = (input("Enter a number: "))

        # if int(number) > 0:
        #     if str(number)[::-1] == number:
        #         print(f"number: {int(number)} is a palindrome")
        #     else:
        #         print(f"number: {int(number)} is not a palindrome")    
        # else:
        #     pass        

# check if a word is a palindrome
        # w = input("enter a word: ")

        # if len(w)  > 0:
        #     if w[::-1] == w:
        #         print(f"word: {w} is a palindrome")
        #     else:
        #         print(f"word: {w} is not a palindrome")    
        # else:
        #     print(f"{w} is not a word!")

# Question4: Write a Python program that calculates the Body Mass Index (BMI) and categorizes it into Underweight, Normal weight, Overweight, and Obesity based on standard BMI ranges.
weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(m): "))

# BMI	        Weight Status
# Below 18.5	Underweight
# 18.5—24.9	    Healthy Weight
# 25.0—29.9	    Overweight
# 30.0 and      Above Obesity


def calc_bmi():
    BMI = (weight / (height * height)) 
    if BMI >= 30:
       print(f"BMI: {BMI}; Above Obesity")
    elif BMI >= 25.0 and  BMI <= 29.9:
        print(f"BMI: {BMI}; Overweight")
    elif BMI >= 18.5 and BMI <= 24.9:
        print(f"BMI: {BMI}; Healthy Weight")
    elif BMI <= 18.5:
        print(f"BMI: {BMI}; Underweight")
    else:
        pass                 
calc_bmi()


# Question5: Write a Python program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".
n = [i for i in range(1,101)]
for i in n:
    if i % 3 == 0:
        print("Fizz")
        if i % 5 == 0:
            print("Buzz")
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")

# NB research on python loops