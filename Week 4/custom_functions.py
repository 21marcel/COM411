def listen():
    print("What sound did you hear?")
    sound = input()
    print(f"That was a loud {sound}!")

listen()

def identify():
    print("What lies before us?")
    lies = input()
    if lies == ("A large boulder"):
        print("It's time to run!")
    else:
        print ("Ah we will be fine")

identify()