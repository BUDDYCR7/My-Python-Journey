'''A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local.'''

# A variable created outside of a function is global and can be used by anyone:
x = 300

def myfunc():
  print(x)

myfunc()

print(x)


'''Naming Variables
If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):'''

# The function will print the local x, and then the code will print the global x:
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)


'''Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
The global keyword makes the variable global.'''

# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = 300

myfunc()

print(x)
# Also, use the global keyword if you want to make a change to a global variable inside a function.


# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)


'''Nonlocal Keyword
The nonlocal keyword is used to work with variables inside nested functions.
The nonlocal keyword makes the variable belong to the outer function.'''

# If you use the nonlocal keyword, the variable will belong to the outer function:
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())


'''The LEGB Rule
Python follows the LEGB rule when looking up variable names, and searches for them in this order:

Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace'''

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)