# Lecture 6 - File I/O

names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"Hello {name}")


name1 = input("What's your name? ")
# the second argument "w" (write) enables the open function to open the file in a way that is going to allow to chnage the content 
file = open("names.txt", "w") 
file.write(name1)
file.close()

name2 = input("What's your name? ")
# the second argument "a" (append) enables the open function not to change the variable that it is storing and store it in a lis t
with open("names.txt", "a") as file:
    file.write(f"{name2}\n")


with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello", line)