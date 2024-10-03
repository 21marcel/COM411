print("What type of book is this?")
book = input()
if book == "adventure":
    print("I like adventure books!")
print ("Finished reading book!")


print("Please enter activity to be performed")
activity = input()
if activity == "calculate":
    print("Performing calculations...")
else:print("Performing activity...")
print("Activity completed!")

print("Which direction should I go?")
direction = input(). lower()
if direction == "up":
    print("I am moving in an upward direction!")
elif direction == "down":
    print("I am moving in an downward direction!")
elif direction == "left":
    print("I am moving in an leftward direction!")
elif direction == "right":
    print("I am moving in an rightward direction!")
