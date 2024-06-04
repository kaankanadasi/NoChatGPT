# Lecture 6 - File I/O

# this way whne the program is runned agan, all of the data that is put into the names is lost
names = []
for _ in range(3):
    names.append(input("What's your name? "))
# sorted() enables the names list to be sorted alphabetically
for name in sorted(names):
    print(f"Hello {name}")


# sotring information - open() opens a file that can store information
# this code (lines 13-18) only stores the last input that is given to the 'name1' variable
name1 = input("What's your name? ")
# the second argument "w" (write) enables the open function to open the file in a way that is going to allow to change the content 
file = open("names.txt", "w") 
file.write(name1)
file.close() # close and save the file


# this code doesn't use the function close(), intead uses 'with' that allows you to specify in this context open and close some file
name2 = input("What's your name? ")
# the second argument "a" (append) enables the open function not to change the variable that it is storing and store it in a list
with open("names.txt", "a") as file:
    # \n file açıldığında verilen değerlerin bitişik yazılmasını engelliyor
    file.write(f"{name2}\n")


# r == read -- open("names.txt", "r") == open("names.txt") -- it comes in default
with open("names.txt", "r") as file:
    # readlines() returns a list that the information of the file stores 
    lines = file.readlines() 

for line in lines:
    # rstrip() enables the line to not create an extra new line, similar to print("hello", line, end="")
    print("hello", line.rstrip())


# a simplified version of the code in lines 30-36
with open("names.txt", "r") as file:
    for line in file:
        print("hello", line.rstrip())


# to sort the information in the file
names_data = []
with open("names.txt", "r") as file:
    for line in file:
        names_data.append(line.rstrip())

for name in sorted(names_data):
    print(f"Hello {name}")


# simplified version of the code in 46-52
with open("names.txt", "r") as file:
    for line in sorted(file):
        print("Hello", line.rstrip())


# sorted in reverse - from z to a
with open("names.txt", "r") as file:
    for line in sorted(file, reverse=True):
        print("Hello", line.rstrip())


# splits the inputs and their given infroamtion for instance harry, Gryffindor
with open("names.txt", "r") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")


# assigning two variables at once
with open("names.txt", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")


# sorted version of the code in lines 75-78
students = []
with open("names.txt", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)


# reverse sorted in a different way - dictonary
with open("names.txt", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students = {"name" : name, "house" : house}
        '''
        long version of line 96:
            student_d = {}
            student_d["name"] = name
            student_d["house"] = house
        '''
        students.append(students)

def get_house(student):
    return student["house"]

for student in sorted(students, key = get_house, reverse = True):
    print(f"{student['name']} is in {student['house']}")


# simplified version of line 105-109
for student in sorted(students, key = lambda student: student["house"], reverse = True):
    print(f"{student['name']} is in {student['house']}")
# lambda is a function without a name - (lambda) (parameter): (returned value)


# what if the stored data contains multiple ',' - that would create a bug as we use commas to differantiate the key-value pair
import csv

students_csv = []

with open("names.txt", "r") as file:
    reader  = csv.reader(file)
    for name, house in reader:
        students_csv.append({"name" : name, "house" : house})
    '''
    long version of line 123-124:
        for row in reader:
            students_csv.append({"name" : row[0], "house" : row[1]})
    '''
        
for student in sorted(students_csv, key = lambda student: student["house"], reverse = True):
    print(f"{student['name']} is in {student['house']}")


#
with open("names.txt", "r") as file:
    reader  = csv.DictReader(file)
    for row in reader:
        students_csv.append({"name" : row["name"], "house" : row["house"]})
        
for student in sorted(students_csv, key = lambda student: student["house"], reverse = True):
    print(f"{student['name']} is in {student['house']}")


#
name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.scv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])


#
with open("students.scv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})