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

print("Please enter a whole number")
number = int(input())
if number % 2 == 0:
    print("This number is an even number!")
else:
    print("This number is an odd number!")

print("Please enter your first number")
x = int(input())
print("Please enter your second number")
y = int(input())
if(x>y):
    print("The first number is greater than the second number!")

