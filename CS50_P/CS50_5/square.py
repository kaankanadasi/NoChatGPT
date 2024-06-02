# Lecture 5 - Unit Tests

def main():
    x = int(input("What's x* "))
    print("x squared is ", square(x))

def square(n):
    return n * n

# to make sure when we import the square funciton in another file, main is not automatically called by itself 
if __name__ == "__main__":
    main()