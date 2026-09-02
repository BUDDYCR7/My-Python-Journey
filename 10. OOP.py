# Code 1
class Enemy:

    def __init__(self,health,attack,movementspeed):
        self.health = health
        self.attack = attack
        self.movementspeed = movementspeed

enemy1 = Enemy("100","Ground",16)
enemy2 = Enemy("70","Air",10)

print ("Giant Stats")
print ("Health:", enemy1.health)
print ("Attack:", enemy1.attack)
print ("Movementspeed:", enemy1.movementspeed)

print ("Balloon Stats")
print ("Health:", enemy2.health)
print ("Attack:", enemy2.attack)
print ("Movementspeed:", enemy2.movementspeed)


# Code 2
class Myself:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

intro = Myself("Shivam",20,"Python")

print ("My name is", intro.name)
print (intro.age)
print (intro.course)


# Code 3
class Weapon:       # This creates a class named "Weapon". A class is like a blueprint or template for creating objects. Here, "Weapon" is the blueprint.
    def __init__(self,name,damage,ammo):        # "def" Means you're defining a function.
    # "__init__" is called the constructor. More specifically, it is Python's initializer method. Its job is to initialize an object.
    # "self" represents the current object being created. "DE" becomes "self". So "self" means the current object.

        self.name = name        # This creates an instance variable called "name". It stores "Desert Eagle" inside the object.
        self.damage = damage        # This creates an instance variable called "damage". It stores "200" inside the object.
        self.ammo = ammo        # This creates an instance variable called "ammo". It stores "7" inside the object.

DE = Weapon("Desert Eagle",200,7)       # This creates an object. Memory is allocated. Then Python automatically calls "__init__(DE,"Desert Eagle",200,7)". which fills the object. So now "DE" contains "Name = Desert Eagle", "Damage = 200", "Ammo = 7".

print ("Name:", DE.name)     # Python looks inside "DE". Finds "name = "Desert Eagle". Prints "Name: Desert Eagle".
print ("Damage:", DE.damage)     # Python looks inside object. Finds "damage = 200". Prints "Damage: 200".
print ("Ammo:", DE.ammo)     # Prints "Ammo = 7".


class Character:
    
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

player = Character("Soldier", 100, "Desert Eagle")
enemy = Character("Devil", 1000, "Katana")

print ("Player: ", player.name)
print ("Health: ", player.health) 
print ("Weapon: ", player.weapon)

print ("Player: ", enemy.name)
print ("Health: ", enemy.health) 
print ("Weapon: ", enemy.weapon)


class Player:
    def __init__(self,mana):
        self.mana = mana  # Instance Variable

player1 = Player(100)
print ("Mana: ", player1.mana)


class Player:

    game_name = "Battle Arena"  # Class Variable (game_name) 

    @classmethod
    def show_game(cls):

        print(cls.game_name)  # Current class

Player.show_game()


class Weapon:

    def __init__ (self, name, damage):
        self.name = name
        self.damage = damage

a = Weapon("AK47", 70)

print (a.name, a.damage)


# Encapsulation
class Golem:
    def __init__(self):
        self.__health = 1000

    def take_damage (self,damage):
        self.__health -= damage

    def show_health(self):
        print (self.__health)

Troop = Golem()

Troop.take_damage(645)
Troop.show_health()


# Inheritance.
class Dragon:
    def move (self):
        print ("Troops are Moving")

class Giant(Dragon):
    def walk (self):
        print ("Giants are Walking")

a = Giant()
a.move()
a.walk()


# Polymorphism
class Warrior:

    def attack(self):
        print("Sword Attack")


class Archer:

    def attack(self):
        print("Arrow Attack")


players = Warrior(), Archer()

for player in players:
    player.attack()


'''self is not a keyword.
It is simply the conventional name Python programmers use for the current object.'''
class Student:
    def study(self):
        print("Student is studying")

student1 = Student()
student1.study()


# #__init__() is a special method that Python calls when an object is initialized.
class Student:
    def __init__(self):
        print("Student is studying")

student1 = Student()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print (f"My name is {name},")
        print (f"I am {age} years old.")

p1 = Person("Shivam", 21)