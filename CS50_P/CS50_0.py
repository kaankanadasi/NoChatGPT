# Lecture 0 - Functions, Variables

name = input("What's your name? ")
# remove whitespace from str + capitilizes each word first letter
name = name.strip().title()

# " " is created by default when passing two arguments to the print() function
# documentation - print(*objects, sep=' ', end='\n')
print("hello", name) 

print("hello ", end = "")
print(name)

print("hello", name, sep = "-")

print(f"hello {name}")

x = float(input("What's x: "))
y = float(input("What's y: "))
z = round(x + y)
m = round(x/y, 2) # rounding the 2nd digit
n = round(x / y)
print(f"{z:,}") # to format the numbers - :,
print(m) 
print(f"{n:.2f}") # rounding the 2nd digit


# main()'i function olarak yazmasaydım hello function'ununu her zaman yukarıda yazmam gerekirdi
def main():
    name_hello = input("What's your name? ")
    hello(name_hello)
    hello()

def hello(to = "world"): # = "world" enables a defualt parameter called "world"
    print("hello", to)

main() 


"""
ERROR EXAMPLE - scope error, name only exist in main

def main():
    name_hello = input("What's your name? ")
    hello()

def hello(): 
    print("hello", name_hello)
"""
def main_2():
    name_h = input("What's your name? ")
    hello(name_h)

def hello(to = "world"): 
    print("hello", to)

main_2()


def main_3():
    x = int(input("What's x? "))
    print("x square is", square(x))

def square(n):
    return n ** 2

main_3()