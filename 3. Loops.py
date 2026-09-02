# While Loops
i = 1
while i <= 6: #stopping condition
    print (i)
    i +=1


i = 5
while i >= 1:
    print (i)
    i -=1


i = 1
while i <= 10:
    print (3*i)
    i +=1


list = [1, "Shivam", False, "Iram", "Vinay"]
i = 0
while i <len(list):
    print (list[i])
    i += 1


# Print table using "while" loop
table = int (input ("Enter the number of table: "))
i = 1
while i < 11:
    print (f"{table} x {i} = {table * i}")
    i += 1


# Sum of number
number = int (input ("Enter the number: "))
i = 1
sum = 0 
while i <= number:
    sum += i
    i += 1

print (sum)


# For Loops
# Print table using "for" loop
table = int (input ("Enter the number of table: "))
for i in range (1, 11):
    print (f"{table} x {i} = {table * i}")


num = int (input ("Enter a number: "))

for i in range (2, num):
    if num % i == 0:
        print (f"{num} is not a prime number")
        break
else:
    print (f"{num} is a prime number ")


# Factorial
num = int (input ("Enter factorial number: "))
product = 1
for i in range (1, num+1): # if we write range "1 to num", range goes to "num-1", but we want to go to "num", so we write "num+1".
    product = product * i

print (f"The factorial of {num} is {product}")