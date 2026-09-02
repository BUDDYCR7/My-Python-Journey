# Print numbers 1-20.
for i in range (1,21):
    print (i)


# Print even numbers.
for i in range (2,21):
    if i % 2 == 0:
        print (i)


# Find the largest number.
numbers = [25, 70, 15, 90, 40]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print (largest)


# Count vowels in a word.
word = input("Enter the word: ")
count = 0
for letter in word:
    if letter.lower() in "aeiou":
        count += 1
print ("Total vowels: ", count)


# Reverse a string.
Word = "Yadav"
ch = Word[::-1]
print (ch)


# Sum a list.
numbers = [7, 10, 11]
total = 0
for i in numbers:
    total += i
print (total)


# Find the maximum number in a list.
numbers = [25, 70, 15, 90, 40]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print (largest)


# Print a multiplication table.
table = int (input ("Enter a number: "))
for i in range (1,11):
    print (table, "x", i, "=", table*i)


# Check whether a number is prime.
prime = int(input("Enter a number: "))
if prime <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, prime):
        if prime % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")


# Sum of a list.
data = [4, 5, 6]
total = 0
for i in data:
    total += i
print (total)


# Find the largest number in a list.
num = [10, 20, 30]
largest = num[0]
for i in (num):
    if i > largest:
        largest = i
print (largest)


# Calculate the factorial of a number.
def factorial_iterative(n):
   if n < 0:
       raise ValueError("Factorial is not defined for negative numbers")
   result = 1
   for i in range(1, n + 1):
       result *= i
   return result


# Example usage
number = int (input("Enter a number: "))
print(f"The factorial of {number} is: {factorial_iterative(number)}")