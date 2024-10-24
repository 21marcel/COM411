
# steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
#
# for i in range (len(steps)):
#     print(steps[i])


print("Moving...")

path=["Move Forward",10, "Move Backward",5, "Turn Left",3, "Turn Right",1]
for i in range(0, len(path) , 2):
     print(f"{path[i]} for {path[i+1]} steps")
