# Lecture 4 - Libraries

# module is a library that has one or more funcitons or other features built into it
import random

coin = random.choice(["heads", "tails"]) # the choice funciton is in the random module
print(coin)


# 'from' is a keyword to importing functions in a module
from random import choice
# now the choice function si in the scope of the file
coin = choice(["heads", "tails"])
print(coin)

number = random.randint(1, 10)
print(number)


cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)



import statistics

print(statistics.mean([100, 90]))



import sys

print(sys.argv[0]) # prints the name of the file 'CS50_4.py'
try: 
    print("hello, my name is", sys.argv[1]) # takes a command line argument - if nothign si types error occurs
except IndexError:
    print("Too few arguments")


if len(sys.argv) < 2:
    print("Too few arguemnts")
elif len(sys.argv) > 2:
    print("Too many arguemnts")
else:
    print("hello, my name is", sys.argv[1])


if len(sys.argv) < 2:
    sys.exit("Too few arguemnts")
elif len(sys.argv) > 2:
    sys.exit("Too many arguemnts")
print("hello, my name is", sys.argv[1])

# taking a subset of a list - slice (since the first elemnt is CS50_4.py)
for arg in sys.argv[1:]:
    print("hello, my name is", arg)



# API - application programming interface
import requests
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
print(json.dumps(response.json(), indent = 2))

o = response.json()
for result in o["results"]: # the json object has a key called results which is a list
    print(result["trackName"])