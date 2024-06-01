# Lecture 2 - Loops

i = 0
while i < 3:
    print("loop")
    i += 1

for _ in range(3):
    print("loop")

print(("loop\n") * 3, end = "")


def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            return n

def loop(n):
    for _ in range(n):
        print("loop")

def main():
    number = get_number()
    loop(number)
 
main()


numbers = [10, 20, 30]

for num in numbers:
    print(num)

for i in range(len(numbers)):
    print(f"index {i}: {numbers[i]}")


# dictionaries
students = {
    "Hermonie": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(students["Hermonie"])

for student in students:
    print(student, students[student], sep = ", ")


students_advanced = [
    {"name": "Hermonie", "house": "Gryffindor", "patronus": "Otter"}, 
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrir"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for std in students_advanced:
    print(std["name"], std["house"], std["patronus"], sep = ", ")


"""
def print_square(size):
    # for each row in square
    for _ in range(size):
        # for each brick in row
        for _ in range(size):
            # print brick
            print("#", end = "")
        # adding new line at the end of the row
        print()
"""
def run():
    print_square(3)

def print_square(size):
     for _ in range(size):
         print("#" * size)

run()