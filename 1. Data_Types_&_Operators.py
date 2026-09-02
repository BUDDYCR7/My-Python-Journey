print ("Hello World")


name = "Shivam"
age = 21
print ("Name:", name)
print ("Age:", age)


a = 5
b = 5
print ("Sum =",a+b)


a = input ("How are you: ")
print ("Me Too")


c =  int (input ("First number: "))
m =  int (input ("Second number: "))
print ("Sum =",c/m)


# Side of Square
a = int (input ("Side one: "))
b = int (input ("Side Two: "))
print ("Sides of a Square:",a*b)


# Print Average
s = float (input ("First Number: "))
z = float (input ("Second Number: "))
print ("Average:", s+z/2)


# True or False
a = input ("Number One: ")
b = input ("Number Second: ")
print (a>=b)


# Equal to
x = int (input ("Num: "))
y = int (input ("Num: "))

print ("Answer: ", x==y)


# Relational/Comparision Operator
a = 1
b = 5
print (a==b)


# Assignment Operator
x=4
x*=27
print (x)


# Identity Operator
c=50
d=90
print (c is not d)


list = [2,3,4,5,6,7,]
print (10 not in list)


i = 22
print (22 is i)


Name = "yadav shivam"
print (Name.find("shivam"))


s = [1,2,3,4,5,6,7,8,9,]
print (s [1:7])


# Slicing
marks = [2,3,4,5,6,]
print (marks [1:3])


mean = {
    "table" : ["a piece of furniture", "list of facts and figures"],
    "cat" : "a small animal",
}
print (mean)


subjects = {
    "python", "c++", "c", "java", "javascript", "python", "java", "c++",
}
print (len(subjects))


marks = {}

x= int (input("enter phy: "))
marks.update({"phy: " :x})

x= int (input("enter math: "))
marks.update({"math: " :x})

x= int (input("enter chem: "))
marks.update({"chem: " :x})

print (marks)


# Truth table of 'or'
print ("True or False is ", True or False)
print ("True or True is ", True or True)
print ("False or True is ", False or True)
print ("False or False is ", False or False)

# Truth table of 'and'
print ("True and False is ", True and False)
print ("True and True is ", True and True)
print ("False and True is ", False and True)
print ("False and False is ", False and False)

# Table of 'not'
print (not(True))
print (not(False))