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


# this way the code still support string like "kaankanadasi@@@gmail.com"
# [] - set of characters
# [^] - complementing the set
if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
# [^@] == anything except an @ sign


# [a-z] means you can only write characters from the alphabet from a through z
# A-Z is for uppercase letters
# 0-9 is for all numbers
# _ 
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")


# \w is for representing a word character, this code is same as in lines 62-65
if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")


# \d decimal digit
# \D not a decimal digit
# \s whitesapce characters
# \S not a whitesapce characters
# \w word character ... as well as numbers and underscores
# \W not a word character


# this now also accepts .edu or .com or .gov at the end of the string
# also we added .lower() in the second  parameter since emails should be in lower case
if re.search(r"^\w+@\w+\.(edu|com|gov)$", email.lower()):
    print("Valid")
else:
    print("Invalid")


# this way by eliminating .lower() and adding a thrid parameter, if we don't want to chamge the users input but ignore case 
if re.search(r"^\w+@\w+\.(edu|com|gov)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# this way the code does not vlaidate codes that has dots after or before the @ sign
# (\w+\.)? means we can have a dor after a word character and by adding '?' it can have 0 or more repetitions 
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|gov)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")



# cleaning users input
name = input("What's your name? ").strip()
# if the user writes something like Kaan, Kanadaşı
if "," in name:
    last,  first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")
# however this code breaks of when we dont have a space after the comma like Kaan,Kanadaşı -> Value Error


# if writer writes Kanadaşı,Kaan 
# ', *' states that we can have 0 or more whitespace after comma
name = input("What's your name? ").strip()
matches = re.search(r"(^.)+, *().+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"hello, {name}")

# or

name = input("What's your name? ").strip()
# we put the assignment statement inside if and changed the '=' to ':=' to still assign the value to matches
if matches := re.search(r"(^.)+, *().+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")



# we want to get the username from a url
url = input("URL : ").strip()
username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")

# using the re library
username_r = re.sub(r"https://twitter.com/", "", url)

# we added ^sicne the stirgn that we are trying to replace is at the start of the string 
# . before the com means that the user can type anyhting in the comntext of re library, so we should change it to \.
# since the https could be http we add a ? before the s
# if we are in the world wide web there could be www. so we add (www\.)?
# https?:// is optional so we add (https?://)?
username_r = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

# the username will be in the .+ part so we add paranthesis to capture that username
if matches := re.search(r"https?://(www\.)?witter\.com/(.+)$", url , re.IGNORECASE):
    # we call mathces.group(2) sicne we have two matches, first match - (www\.) and the second match (.+) which is the usernmae
    print(f"hello, {matches.group(2)}")

# since we don't want to capture the first group and ignroe the parnthesis we use the synthx (?:...)
if matches := re.search(r"https?://(?:www\.)?witter\.com/(.+)$", url , re.IGNORECASE):
    print(f"hello, {matches.group(1)}")