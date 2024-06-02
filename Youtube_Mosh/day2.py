price = 10 # when you intialize the price variable in the computers memory, the computer will store this value in binary - 0s and 
print("*" * price)

name = input("What is your name? ")
print("Hi " + name)

import datetime # to get the current year
birth_year = int(input("Birth year: "))
age = datetime.date.today().year - birth_year
print("your age is " + str(age))
print(type(age)) # <class 'int'>

course = '''Hi Kaan, 
This is a multiline string for you.
Keep going.'''
print(course[0]) # prints the first character
print(course[-1]) # prints the last character 
print(course[10:-5])
print(course[1:4])
print(course[:3])
print(course[10:])
print(course[:])
 
first = "John"
last = "Smith"
message = f'{first} [{last}] is a coder' # formatted string
print(message)

hi = "hello"
hi.replace("h", "H")
hi.upper() # this creates a new string that is not related to the hi variable, thus the for funciton does not print in upper cases
for i in range(len(hi.lower())):
    print(hi[i])
bool_result = "Hello" in hi
print("Hello is in the hi variable: " + str(bool_result)) 

import math
x = 10.9 + 3 * 2 ** 2 #22.9
rounded = round(x) #23 
floored = math.floor(x) #22
y = abs(-3)

secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess:" ))
    guess_count += 1
    if guess == secret_number:
        print("You won")
        break
else:
    print("Sorry, you failed")


for item in "Python":
    print(item)

for i in ["Python", "Java", "SQL"]:
    print(i)

for i in range(10):
    print(i)

for i in range(5, 15, 3):
    print(i)

prices = [10, 20, 30] 
total = 0
for price in prices:
    total += price
print(f"Total: {total}")


for x in range(2):
    for y in range(5):
        print(f"({x},{y})")

numbers = [5, 2, 5, 2, 2]
numbers.sort()
for item in numbers:
    output = ""
    for i in range(item):
        output += "x"
    print(output)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
] 
matrix.insert(0, [-2, -1, 0])
matrix.pop()
for row in matrix:
    for item in row:
        print(item)
matrix.clear()
print(matrix)

list = [30, 40, 4, 2, 4, 30]
new_list = list.copy() # the changes made into this list will not affct the original list

# removing duplicates 
uniques = []
for item in list:
    if item not in uniques:
        uniques.append(item)

# touples - we cannot change touples, only get information about the toples
coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x, y, z = coordinates # unpacking - this would also work in list


# dictionaries
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"]) # John Smith
print(customer["birthday"]) # ERROR
print(customer.get("name")) # John Smith
print(customer.get("birthday")) # NONE
print(customer.get("birthday", "Jan 1 1990")) # Jan 1 1990

customer["birthday"] = "Jan 1 1990"
print(customer["birthday"])


phone = input("Phone: ")
num = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eigth",
    "9": "nine"
}
output = ""
for i in phone:
    output += num.get(i) + " "


def greet_user(name):
    if name == None:
        name = "user"
    print(f"Hi {name}")
    print("Welcome aboard")
greet_user("John")

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")
greet_user(last_name = "Smith", first_name = "John") # keyword arguments

def square(number):
    return number * number

def squareP(number):
    print(number * number)
print(squareP(3)) 
# 9
# None
# by defualt if we don't have a return statemenet, all functions return the value None (null)


# exceptions
try:
    age = int(input("Age: "))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("Invalid Value")


# classes
class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")
point1 = Point()
point1.draw()
point1.x = 10 # attribute x
point1.y = 20 # attribute y

class Point:
    def __init__(self, x, y): # constructor
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")


# inheritance
class Mamal:
    def walk(self):
        print("walk")
class Dog(Mamal):
    pass # sicne the python interperter doesn't like empty classes, we use pass statement to say pass this line
dog1 = Dog()
dog1.walk()


#modules
import Youtube_Mosh.day2_example as day2_example
from Youtube_Mosh.day2_example import func

print(day2_example.func())
print(func())


# random
import random
for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

members = ["John", "Mary", "Bob"]
leader = random.choice(members)

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return (first, second)
dice = Dice()
print(dice.roll())