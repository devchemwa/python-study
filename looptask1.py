# 1. Write a program that displays a numbers 1 to 50 inside a list.
# importing math
import math
l = [i for i in range(1,51)]
print(l)
#2. From 1 above display the ones divisible by 7 or 5 inside a list.
for i in l:
    if i % 7 == 0 and i % 5 == 0:
        n = []
        n.append(i)
print(n)

#3. Find sum and average of values in the range between 10 to 40.
s = sum(range(10,41))
avg = (s / len(range(10,41)))
print(f"sum: {s}, Average: {avg}")


#4. Put in a list the first 10 odd numbers between 10 to 50. 
odd = []
counter = 0
for i in range(10,51):
    pass
    if i % 2 != 0:
      counter += 1
      odd.append(i)
      if counter == 10:
        print(odd)


#5. write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
number = int(input("Enter a number: "))
t = 1
results = []
for i in range(1, 11):
    if number >= 0:
        q = number * t
        results.append(q)
        t += 1
        if t == 11:
          print(results)

#6. write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
even = [f for f in range(1,51)]
count = 0
for f in even:
     if f % 2 == 0:
        count += 1
        print(f,f"count: {count}")

# ls1 = [ ("Jay", 20), ("Mo", 30), ("Mya", 32) ]
#7. Display the total quantity of the 3 above.
ls1 = [ ("Jay", 20), ("Mo", 30), ("Mya", 32) ]
total = 0
for a,b in ls1:
    total += b

print(f"total: {total}")
