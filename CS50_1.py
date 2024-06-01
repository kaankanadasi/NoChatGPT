# Lecture 1 - Conditionals

def Score():
    score = int(input("Score: "))
    if score >= 90:
        return "Grade A"
    if score >= 80:
        return "Grade B"
    if score >= 70:
        return "Grade C"
    if score >= 60:
        return "Grade D"
    return "Grade F"

print(Score())


def is_even(n):
    return n % 2 == 0


name = input("What is your name? ")

match name:
    case "Harry" |  "Hermonie" | "Ron": # '|' is for 'or'
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # undescore '_' means for any case that is not handled (else)
        print("Who?")