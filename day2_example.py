def func():
    stopped = True
    started = False
    while True:
        command = input("> ").lower()
        if command == "help":
            print("""
    start - to start the car
    stop - to stop the car
    quit - to exit
                """)
        elif command == "start":
            if started:
                print("The car is already started.")
            else:
                started = True
                stopped = False
                print("Car started...Ready to go!")

        elif command == "stop":
            if stopped:
                print("The car is already stopped.")
            else:
                started = False
                stopped = True
                print("Car stopped.")
            
        elif command == "quit":
            break
        else:
            print("I don't understand that...")
