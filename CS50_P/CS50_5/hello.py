def main():
    name = input("What's your name* ")
    print(hello(name))

def hello(to = "world"):
    return "hello " + to

if __name__ == "__main__":
    main()