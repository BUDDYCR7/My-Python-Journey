def my_function(*kids):
  print("The youngest child is", kids[1])

my_function("Emil", "Tobias", "Linus")


def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")


'''Using *args with Regular Arguments
You can combine regular parameters with *args.
Regular parameters must come before *args:'''
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")
# In this example, "Hello" is assigned to greeting, and the rest are collected in names.


# A function that calculates the sum of any number of values
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


# Finding the maximum value
def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))


'''Unpacking Arguments
The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
Unpacking Lists with *
If you have values stored in a list, you can use * to unpack them into individual arguments:

Using * to unpack a list into arguments:'''
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers)
print(result)


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