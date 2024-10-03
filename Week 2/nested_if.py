print("What type of cover does the book have?")
cover = input()
if cover == "soft":
    print("Is the book perfect bound?")
bound = input()
if bound == "yes":
    print("Soft cover, perfect bound books are very popular")
elif cover == "hard" :
    print("Books with hard covers can be more expensive")
else:
    print("Soft covers with coils or stitches are great for short books")


response= input("Where should I look?")
if response == "in the bedroom":
    bedroom = input("Where in the bedroom should I look?")
    if bedroom == "under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone")
elif response == "in the bathroom":
    bathroom = input("Where in the bathroom should I look?")
    if bathroom == "in the sink":
        print("Found some hair but no phone")
    else:
        print("Found some bathroom stuff but no phone")
elif response == "in the living room":
    living_room = input("Where in the living room should I look?")
    if living_room == "on the table":
        print(" I found my phone")
    else:
        print("Found some stuff but no phone")
