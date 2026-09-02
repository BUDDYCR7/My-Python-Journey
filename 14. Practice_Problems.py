# Printing Pattern
def pattern():
    print ("-" * 30)
    
print ("Menu")
pattern()
print ("1. Start")
print ("2. Exit")
pattern()


def enemy_name():
    return ["Archer", "Wizard", "Golem", "Barbarian", "Giant"]

print(enemy_name())


'''
*args. (Non-keyword/Positional Arguments).
*args collects  extra positional arguments into a tuple.
'''
def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    print (total)
    
add (20,74)


'''**kwargs. (Keyword Arguments).
**kwargs collects extra keyword arguments into a dictionary.
'''


# Write a function to print your name.
def name():
    return "Shivam"
    
result = name()
print (result)


# Write a function that adds two numbers.
def add(num1, num2):
    return num1 + num2
    
result = add(23,67)
print (result)


# Create a function with a default argument.
def info(name, country = "India"):
    return name, country

result = info("Shivam")
print (result)


# Create a function that returns the square of a number.
def square(num):
    return num * num
    
result = square(5)
print (result)


# Demonstrate the difference between local and global variables.
v = 45
def show():
    return v
    
result = show()
print (result)


# Global.
x = 15 
def value():
    global x
    x = 2026
    return x
    
result = value()
print (result)


# Create a nested function that prints two messages.
def fun_1():
    return "Hi"
def fun_2():
    return "Shivam"

result = fun_1(), fun_2()
print (result)