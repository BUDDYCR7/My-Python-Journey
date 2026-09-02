# Function Definition
def enter(): # "()" Parentheses", Used for parameter. ":" Colon tells Python a block starts here.
    c = input ("Welcome: ")
    print ("Hi", c)
enter() # Function Call, calling a Function. It means when you want to run or execute it.


# Calling a Function
def greet():
    print("Hello")
greet() # Calling a Function.


# Use parameter names. Advantages:- More readable, Order doesn't matter, Easier for large functions.
def employee(name, salary, department): # Defining a function. "employee" Function name, choose a meaningful name.
    print(name)
    print(salary)
    print(department)
employee(department="IT", salary=50000, name="Shivam") # Parameter names. Function called.


def add():
    a = int (input ("Enter the first number: "))
    b = int (input ("Enter the second number: "))
    print(a+b)
    print(a*b)
    print(a-b)
    print(a/b)
    print(a%b)
add()


def sum (a, b):
    s =a+b
    return s
print (sum(27,69))
print (sum(2978,3876))
print (sum(265,399))
print (sum(88,1))
print (sum(7654,89))
print (sum(266,898))
print (sum(2,76))


def add (a, b):
    result = a + b
    print(result)

add(13, 2)


# **kwargs
def student(**details):
    print(details)
student(name="Shivam", age=22)


# **kwargs
def student(**details):
    for key, value in details.items():
        print(key, value)
student(name="Shivam", age=22,city="Mumbai",phone=9876543210)


# Positional
def add(a, b):
    return a + b
# Keyword
def student(name, age):
    print(name, age)
# Default
def greet(name, country="India"):
    print(name, country)
# *args
def total(*nums):
    print(sum(nums))
# **kwargs
def profile(**data):
    for key, value in data.items():
        print(key, ":", value)


# recursion
# factorial(number) = number * factorial(n-1)
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

print (factorial(6))


# My Practice Solution.

# Positional Arguments.
# Create a function introduce(name, age),
# Call the function using positional arguments.
def introduce(name, age):
    print (name)
    print (age)
    
introduce("Shivam",22)


# Keyword Arguments.
# Create a function student(name, course),
# Call it using keyword arguments.
def student(name, course):
    print ("Name:", name)
    print ("Course:", course)
    
student(name = "Shivam", course = "Python")


# Default Arguments
# Create a function, greet(name, message="Good Morning")
def greet (name, message="Good Morning"):
    print (name, message)
    
greet ("Shivam" ",")


# Default Arguments, Override the default.
# Create a function, greet(name, message="Good Morning")
# Override the default
def greet (name, message="Good Morning"):
    print (name, message)
    
greet ("Shivam" ",")
greet ("Imran"+",", "Good Night")


# Write a lambda function that returns the square of a number.
num = lambda x: x*x
print (num (5))


# Create a lambda function to add two numbers.
add = lambda x,y : x+y
print (add (144,62))


# Given two numbers, return the larger one.
larger = lambda a,b : a if a>b else b
print (larger (2678,890))


# Check Even or Odd.
find = lambda i : "Even" if i % 2 == 0 else "Odd"
print (find (3))


# Multiply three numbers.
ai = lambda c,i,d : c*i*d
print (ai (13,14,34))


def calcute_age():
    age = 18
    if age >= 18:
        print ("Adult")
    else:
        print ("Minor")
calcute_age()


def mark_sheet(english, math, hindi):
    print (english)
    print (math)
    print (hindi)
mark_sheet(english = 789, math = 499, hindi = 148)


# Write a function greet(name) that returns:
def greet(name):
    print ("Hello", name)
greet(name = "Alice")


# Write a function square(n) that returns the square of a number.
def square():
    side = int (input("Enter the Number: "))
    print (side * side)
square()


# Write a function add(a, b) that returns the sum of two numbers.
def add(a,b):
    print (a+b)
add(a=4, b=4)


# Write a function is_even(n) that returns True if the number is even, otherwise False.
def even():
    a = int (input("Enter the Number: "))
    if a % 2 == 0:
        print ("EVEN")
    else:
        print ("ODD")
even()


def pattern():
    print ("-"*30)
    
print ("Menu")
pattern()
print ("End")
pattern()


"""Best Example on "retun",  Write a function largest(a, b, c) that returns the largest of three numbers.""" # This is a docstring (a multi-line string).
"""return" does two things: Sends a value back to the caller. Stops the function immediately. Nothing after it inside the function runs."""

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def square(number):
    return number * number

largest_number = largest(10, 20, 30)
print("Largest number:", largest_number)

result = square(largest_number)
print("Square:", result)


# return
def circle_stats(radius):
    return 3.14 * radius ** 2  # "return" statement ends the function execution. The "HI" will never be execute inside the function

print (circle_stats(10))


# Write a function that greets a user
def greet(name = "Imran"):
    return name
    
print (greet())
print (greet("Tarik"))


# Global and Local Variable
username = "Shivam" # Global Variable

def funcation():
    username = "yadav" # Local Variable
    
print (username)
funcation()


num_1 = 10
def sum(num_2):
    num_final = num_1 + num_2
    return num_final
    
Final = sum(30)
print (Final)


x = 99
def func():
    global x
    x = 7
    
func()
print (x)


wheather = (input("Enter the wheather: "))

def icecream():
    if wheather == "sunny" or wheather == "hot":
        return ("Buy an Ice-cream")
    elif wheather == "rainy":
        return ("Avoid eating an Ice-cream")
    elif wheather == "winter" or wheather == "cold":
        return ("Ice-cream is not allowed")
    else:
        return("Invalid")
        
Result = icecream()
print (Result)


# Write a python program using function to convert Celsius to Fahrenheit
def convert(f):
    return 5 * (f-32) / 9
    
f = float (input ("Enter temperature in F: "))
Result = convert(f)
print (f"{round (Result, 2)} °C")


# Sum Numbers
def sum(n):
    if n ==1:
        return 1
    return sum(n-1) - n
    
print (sum(5))