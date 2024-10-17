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

def escape_by(plan):
    if plan == "Jumping over":
        print("We cannot escape that way!The boulder is too big!")
    elif plan == "Running around":
        print("We cannot escape that way!The boulder is moving too fast!")
    elif plan == "Cross bridge ahead":
        print("We cannot escape that way!The boulder is in the way!")

escape_by("Jumping over")
escape_by("Running around")
escape_by("Cross bridge ahead")


