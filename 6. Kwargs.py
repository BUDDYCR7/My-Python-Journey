'''If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
This way, the function will receive a dictionary of arguments and can access the items accordingly:'''
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


'''The **kwargs parameter allows a function to accept any number of keyword arguments.
Inside the function, kwargs becomes a dictionary containing all the keyword arguments:'''
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")


'''You can combine regular parameters with **kwargs.
Regular parameters must come before **kwargs:'''
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print("  ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")


'''You can use both *args and **kwargs in the same function.
The order must be:
regular parameters
*args
**kwargs'''
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")


'''Unpacking Dictionaries with **
If you have keyword arguments stored in a dictionary, you can use ** to unpack them:

Using ** to unpack a dictionary into keyword arguments:'''
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)


'''Real-Life Analogy

Imagine a delivery box.
Inside:
Apple
Banana
Mango

Without unpacking:
You hand the entire box to the function.
Function(box)

With unpacking:
You take each fruit out individually.
Function(Apple, Banana, Mango)

That's exactly what * does.'''