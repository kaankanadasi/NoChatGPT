# Lecture 3 - Exceptions

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")


# else olmasaydı NameError oluşabilirdi - eğer inputa stirng literal koyulsaydı, input int olmadığından dolayı initlize olmazdı
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}") 
 

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}") 


while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")
print(f"x is {x}") 


# The pass statement is a null operation; it does nothing when executed. It's used as a placeholder 
# in situations where a statement is syntactically required but you don't want to execute any code
def get_int():
    while True:
        try:
            return int(input("What's x? ")) # eğer ValueError varsa return statementına gelmeden program catch ediyor
        except ValueError:
            pass


from datetime import datetime
current_year = datetime.now().year

def valid_input(prompt):
    while True:
        try:
            birth_year = int(input(prompt))
            if birth_year < 1900 or birth_year > current_year:
                print("Please enter a valid year.")
                # To skip the remaining code inside the current iteration of a loop and immediately move on to the next iteration
                continue 
            return birth_year
        except ValueError:
            print("Please enter a valid year.")

y = valid_input("What's your birth year? ")
print(f"your age is {current_year - y}")