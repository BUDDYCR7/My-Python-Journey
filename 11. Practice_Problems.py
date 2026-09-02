# Take your name as input.
name = input ("Enter your name: ")
print ("Hello", name)


# Take two numbers. 
a = int (input ("Enter first number: "))
b = int (input ("Enter second number: "))
print (a+b)
print (a-b)
print (a*b)
print (a/b)


# Take age.
age = int (input ("Enter your age: "))
if age >= 18:
    print ("Eligible for Vote")
else:
    print ("Not Eligible")


# Loop through numbers
for i in range(51):
    print (i)


# Loop through user input. Loop through numbers
num = int (input("Enter the number: "))
for i in range(num): # when taking input the "num" becomes the value entered by the "user".
    print (i)


# Print numbers from 0 to 9.
for i in range(10):
    print (i)


# Print numbers from 1 to 10.
for i in range(11):
    print (i)


# Ask the user for a number.
data = int (input("Enter number: "))
for number in range(data):
    print (number)


# Take your name as input. Print every letter on a new line.
letter = input ("Your Name: ")
for letters in (letter):
    print (letters)


# Loop through a string
name = (input("Your Name: "))
for letters in (name): # the "i" could be anything python doesn't care.
    print (letters)

for number in range(3):
    print("Python")
    print("Game") # # A for loop repeats the entire indented block, not one line at a time.


# Take a word.
word = input ("Enter your Word: ")
print (len(word))


# Take a word. Print every letter with its own message.
software = "Blender"
for letters in (software): # # It is not counting the index. It is taking one character at a time.
    print ("Letter: ",letters)


# What is range(start, stop)?
# By default, range() moves forward. Negative step -1,-2 (Move backward).
# Write a program that prints: 100,90,80,70,60,50,40,30,20,10
for i in range(100, 0, -10):
    print (i)


# Write a program that prints only odd numbers from 1 to 20.
for i in range(1,20):
    if i % 2 != 0:
        print (i)


for i in range (1,15):
    if i % 2 == 0:
        print ("Level",i, ": Weapon Unlocked")


# Here, i is not used.
for i in range(5):
    print("Hello")


# Here, i is the important part.
for i in range(5):
    print(i)


for enemy in range(1, 6):
    print("Enemy", enemy, "Spawned")


for i in range(3):
    print ("*****")


for i in range(1,6):
    print ("*"*i)


for i in range(1,6):
    print ("Loading"+"."*i)


for i in range(1,6):
    print ("Level",i)
print ("Mission Complete!")


# if, elif, else. Remember this forever: Python checks from top to bottom and stops at the first True.
# We usually write conditions from the most specific or highest threshold down to the lowest.
# if/elif checks from top to bottom and stops at the first True condition.
health = int(input("Enter Health: "))
if health > 70:
    print ("Healthy")
elif health > 30:
    print ("Injured")
else:
    print ("Critical")


# Asks the user for the number of bullets.
bullets = int(input("Enter remaining bullets: "))
if bullets < 1:
    print ("Reload")
elif bullets > 10:
    print ("Full ammo")
else:
    print ("Keep Shooting")