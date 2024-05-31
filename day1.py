print("Hello World")
age = 20
true = False
bill = 0.99


name = input("What is your name? ") # getting input
print("Hello " + name)


birthYear = input("What is your birth year? ")
age = 2024 - int(birthYear) # input()un return value'su string olduğundan dolayı int() built-in functionuyla integer a çeviriyoruz
print(birthYear)


first = input("First:")
second = input("Second:")
sum = float(first) + float(second)
# print("Sum " + sum) THIS WOULD GIVE AN ERROR -> JAVA CANNOT UNDERSTAND "Sum" + 19.1
print("Sum " + str(sum))


course = "Python for Begginers"
print(course.upper()) # makes the string upper case HOWEVER this method does not chnage the original string, it will return a new string
print(course) # since the origianl string is not changed it will print "Python for Begginers"
print(course.find('y')) # returns the index of the first occurance of 'y'

# the replace method does not chnaged the original string, it will create a new string object in memory
# AP CS-A'da method yazdığında return edilen string input'taki string'i değiştirmiyordu - bunun gibi düşün
# nedeni - strings are immutable
print(course.replace('for', '4')) # changes the string course to "Python 4 Begginers"
print(course.replace('x', '4')) # nothing is changed, no error

print('python' in course) # returns True


print(10 / 3) # 3.33333333
print(10 / 3) # 3
print(10 ** 3) # 1000


x = 3==3
print(x) # True


price = 25
print(price > 10 and price < 30)
print(price > 10 or price < 30)
print(not price > 10)


temp = 35
if temp > 30:
    print("It's a hot day")
    print("Drink water")
    # iki line da print edilir
elif temp > 20: 
    print("It's a nice day")
elif temp > 10: 
    print("It's a bit cold")
else: 
    print("It's cold")


# example
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else: 
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))


# prints from 1 to 1000
i = 1
while i <= 1_00:
    print(i)
    i += 1

# prints from * (1 *) to ********** (10 *)
i = 1
while i <= 10:
    print(i * '*')
    i += 1


names = ["John", "Bob", "Kane", "Mary", "Sam"]
names[0] = "Jon" # changed the first element to Jon
print(names) # ["Joh", "Bob", "Kane", "Mary", "Sam"]
print(names[0]) # John
print(names[-1]) # Sam - the last element in the list 
print(names[-1]) # Mary - the second last element in the list 
print(names[0:3]) # ["Joh", "Bob", "Kane"] - prints the elemnts from index 0 to 2

numbers = [1, 2, 3, 4, 5] 
numbers.append(6)
numbers.insert(0, -1)
numbers.remove(3)
print(1 in numbers) # checks if 1 is in the numbers list
length = len(numbers)

for i in numbers: 
    print(i) # prints each item in a new line

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

firstNum = range(5)
print(firstNum) # range(0, 5)
for n in firstNum:
    print(n) 

secondNum = range(5, 10, 2)
print(secondNum) # range(5, 10)
for n in secondNum:
    print(n) # prints 5, 7, and 9 on distinc lines


# tuples are immutable
numbers = (1, 2, 3, 3)
# numbers[0] = 10 would give an error sicne we cannot change the value inside a touple after initilization
numbers.count(3) # 2