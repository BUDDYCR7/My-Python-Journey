a = input ("First Name: ")
print ("length of the word is: ", len(a))


b = ("i have 100$, and i paid 50$ to shiv, 20$ to imran, and 10$ to shashank, how much do i have now")
print (b. count("$"))


# Grade students based on marks.
marks = int (input("Enter the marks: "))

if(marks >= 90):
    Grade = "A"
elif(marks >= 80 and marks < 90):
    Grade = "B"
elif(marks >= 70 and marks < 80):
    Grade = "C"
else:
    Grade = "D"

print ("grade of the student ", Grade)


# Nesting
age = 20
# nesting
if (age >= 55):
    if (age >= 11):
        print ("cannot drive")
    else:
        print ("can drive")
else:
    print ("cannot drive")


a = 'shivam'
print (type (a))


name = "Shivam"
age = 22
course = "Python Course"
status = "Learning Stage"

print ("My name is:",name)
print ("I am:",age)
print ("I am doing:", course)
print ("Currently i am in a:", status)


h = "hello"
print (h [1:4])


age = 17

if (age >=18):
    print ("Eligible for Vote")
else:
    print ("Not Eligible for Vote")


age = 17
if (age < 18):
    print("Minor")
elif (age == 18):
    print ("Teen")
else:
   print ("Adult")


age = 17
print("Minor" if age < 18 else "Teen" if age == 18 else "Adult")


Health = 100
print ("Dead" if Health <= 0 else "Alive")


Weapon = "yes"
if(Weapon != "yes"):
    print ("Armed")
else:
    print ("Unarmed")

Weapon = "yes"
print ("Armed" if Weapon!="yes" else"Unarmed")


i = int (input ("Enter your Age: "))
if i >= 18:
    print ("Eligible for Driving")
else:
    print ("Not Eligible for Driving")


i = int (input ("Enter your Age: "))
print ("Eligible for Driving" if i >= 18 else "Not Eligible for Driving")


a = "HI"
b = False
if a == True and b != False:
    print ("True")
elif a == False:
    print ("False")
else:
    print ("INVALID")


a = input ("First Name: ")
print ("length of the word is: ", len(a))


b = ("i have 100$, and i paid 50$ to shiv, 20$ to imran, and 10$ to shashank, how much do i have now")
print (b. count("$"))


# Grade students based on marks.
marks = int (input("Enter the marks: "))

if(marks >= 90):
    Grade = "A"
elif(marks >= 80 and marks < 90):
    Grade = "B"
elif(marks >= 70 and marks < 80):
    Grade = "C"
else:
    Grade = "D"

print ("grade of the student ", Grade)


# Nesting
age = 20
# nesting
if (age >= 55):
    if (age >= 11):
        print ("cannot drive")
    else:
        print ("can drive")
else:
    print ("cannot drive")


a = 'shivam'
print (type (a))


name = "Shivam"
age = 22
course = "Python Course"
status = "Learning Stage"

print ("My name is:",name)
print ("I am:",age)
print ("I am doing:", course)
print ("Currently i am in a:", status)


h = "hello"
print (h [1:4])


age = 17

if (age >=18):
    print ("Eligible for Vote")
else:
    print ("Not Eligible for Vote")


age = 17
if (age < 18):
    print("Minor")
elif (age == 18):
    print ("Teen")
else:
   print ("Adult")


age = 17
print("Minor" if age < 18 else "Teen" if age == 18 else "Adult")


Health = 100
print ("Dead" if Health <= 0 else "Alive")


Weapon = "yes"
if(Weapon != "yes"):
    print ("Armed")
else:
    print ("Unarmed")

Weapon = "yes"
print ("Armed" if Weapon!="yes" else"Unarmed")


i = int (input ("Enter your Age: "))
if i >= 18:
    print ("Eligible for Driving")
else:
    print ("Not Eligible for Driving")


i = int (input ("Enter your Age: "))
print ("Eligible for Driving" if i >= 18 else "Not Eligible for Driving")