#1
def any_num(*nums):
    operator = (input("Enter the operator: "))

    if operator == "sum":
        print (sum(nums))
    elif operator == "max":
        print (max(nums))
    elif operator == "min":
        print (min(nums))
    elif operator == "average":
        print (sum(nums)/len(nums))
    else:
        print ("Invalid")

any_num(10, 48, 58, 75, 93)


#2
def info(**details):
    return details
    
result = info (Name = "Shivam", Age = 20, City = "India", Profession = "Game Artist")

print (result)


#3
def product(*nums):
    total = 1
    for i in nums:
        total *= i
    return total
    
numbers = [10, 20, 30, 40]

result = product(*numbers)
print (result)


#4
def order(customer, *items, **details):
    print ("Customer:" , customer)
    print ("Items:" , items)
    print ("Details:" , details)

order ("Shivam", "Keyboard", "Mouse", "Headphones", Price = 5000, Delivery = "Express")


#5 Takes another function as an argument
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def calculate(a, b, operation):
    return operation(a, b)

print(calculate(10, 5, add))
print(calculate(10, 5, multiply))
print(calculate(10, 5, subtract))


#6 Return another function
def create_multiplier(n):
    def multiplier(x):
        return n * x

    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(10))
print(triple(10))


#6.1 The outer function gives the inner function some information, and the inner function remembers it. That's a closure.
def create_greeter(greeting):
    def greet(name):
        return greeting + " " + name
    
    return greet
    
hello = create_greeter("Hello")
print(hello("Shivam"))


#6.2
def create_power(n):
    def power(x):
        return x ** n
        
    return power
    
result = create_power(2)
print (result(5))


#6.3
def create_discount(percent):
    def discount(amount):
        discount_amount = amount * percent / 100
        return amount - discount_amount
        
    return discount
    
result = create_discount(20)
print (result(1000))


#6.4
def create_counter():
    count = 0

    def counter():
        nonlocal count #tells Python: "Don't create a new local count. Use the count from the outer create_counter() function."
        count += 1
        return count

    return counter
    
result = create_counter()
print (result())
print (result())
print (result())
print (result())
print (result())


#6.5
def create_prefix(prefix):
    def add_prefix(text):
        return prefix + text

    return add_prefix

result = create_prefix("Mr.")
print (result("Shivam"))


#7
def my_filter(function, numbers):
    result = []

    for i in numbers:
        if function(i):
            result.append(i)

    return result

numbers = [1, 2, 3, 4, 5, 6]

def is_even(num):
    return num % 2 == 0

result = my_filter(is_even, numbers)
print(result)


#8
def my_map(function, numbers):
    result = []

    for i in numbers:
        result.append(function(i))

    return result

numbers = [1, 2, 3, 4, 5]

def square(num):
    return num * num

result = my_map(square, numbers)
print (result)


#8.1 my_map() work with a lambda function
def my_map(function, numbers):
    result = []
    
    for i in numbers:
        result.append(function(i))
        
    return result

numbers = [1, 2, 3, 4, 5]

result = my_map(lambda num : num * num, numbers)
print (result)


#8.2
def my_map(function, numbers):
    result = []
    
    for i in numbers:
        result.append(function(i))

    return result

numbers = [1, 2, 3, 4, 5]

result = my_map(lambda num : num + 10, numbers)
print (result)


#8.3
def my_filter(function, numbers):
    result = []

    for i in numbers:
        if function(i):
            result.append(i)

    return result

def my_map(function, numbers):
    result = []

    for i in numbers:
        result.append(function(i))

    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def is_even(num):
    return num % 2 == 0

def square(num):
    return num * num

even_numbers = my_filter(is_even, numbers)
result = my_map(square, even_numbers)

print(result)


#9
def create_account(initial_balance):
    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        balance -= amount
        return balance

    def check_balance():
        return balance

    return {
        "deposit": deposit,
        "withdraw": withdraw,
        "balance": check_balance
    }


account = create_account(1000)

account["deposit"](500)
account["withdraw"](200)

print(account["balance"]())


#10
import time

def timer(function):
    def wrapper():
        start = time.time()
        function()
        end = time.time()

        print(f"{function.__name__} took {end - start:.2f} seconds")

    return wrapper

@timer
def process():
    time.sleep(1)

process()


#10.1
def timer(function):
    def wrapper():
        start = time.time()
        function()
        end = time.time()

        print (f"{function.__name__} took {end-start:.2f} seconds")

    return wrapper

@timer
def test():
    time.sleep(1)

test()


#10.2
def timer(function):
    def wrapper():
        start = time.time()
        function()
        end = time.time()

        print (f"{function.__name__} took {end-start:.2f} seconds")

    return wrapper

@timer
def work():
    total = 0

    for i in range(1000000):
        total += i

work()


#10.3
def timer(function):
    def wrapper():
        print ("Starting work...")

        start = time.time()
        function()
        end = time.time()

        print (f"{function.__name__} took {end - start:.2f} seconds")

        print ("Finished work.")

    return wrapper

@timer
def work():
    total = 0

    for i in range(1000000):
        total += i

work()


#10.4
def timer(function):
    def wrapper(*args):
        start = time.time()
        result = function(*args)
        end = time.time()

        print (f"{function.__name__} took {end - start:.2f} seconds")

        return result

    return wrapper

@timer
def work(a, b):
    return a + b

result = work(10, 20)
print (result)