# Lecture 7 - Regular Expressions

# strip() removes any whitespace that is typed after the answer
email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")


username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")


import re
# . - any character except a newline
# * - 0 or more repetitions
# + - 1 or more repetitions
# ? - 0 or 1 repetition
# {m} - m repetitions
# {m,n} - m-n repetitions

# or use re.search("..*@..*", email)
if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")