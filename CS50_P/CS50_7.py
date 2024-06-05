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
# we use '\' before '.edu' since using '.' in this context would mean a different thing
# yet, since python interperts '\' as new line, we put 'r' before the string to indicate not to create a new line 
if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")


# since we don't want the user to type "my email is kaankanadasi@gmail.com", we should indicate that 
# the mail is in the  should be the start and the end of the string

# ^ - matches the start of the string 
# $ - matches the end of the string or just before the newline at the end of the string
if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")