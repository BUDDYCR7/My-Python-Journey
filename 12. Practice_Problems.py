a = input ("Your Name: ")
print ("Hello,", a)


for i in range(1,6):
    print ("Level", i)


for i in range(5,0):
    print (i)
print ("GO!")


for i in range(1,21):
    if i % 2 == 0:
        print (i)


for i in range(1,21):
    if i % 2 != 0:
        print (i)


for i in range(5,55,5):
    print (i)


for i in range(1,11):
    if i % 2 == 0:
        print ("Level", i," :Weapon Unlocked")


health = int (input("health: "))
if health > 70:
    print ("Healthy")
elif health > 30:
    print ("Injured")
else:
    print ("Critical")


for i in range(1,6):
    print ("#"*i)


# Wrong 
for i in range(1,6):
    print ("="*i)


for i in range (1,6):
    print ("Loading"+"."*i)


word = int (input("How many Levels: "))
for word in range (1, word):
    print ("Level: ",word)