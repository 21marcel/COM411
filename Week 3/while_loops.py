count = 0
print("How many apples should I remove?")
apples=int(input())

while count < apples:
    print("Removed apple")
    count += 1

count = 1
print("How many obstacles must I avoid?")
obstacles=int(input())

while count <= obstacles:
    print(f"Avoiding... Done {count} obstacles avoided")

    count += 1
print("All obstacles have been avoided!")

count = 1
print("How many bars should be charged")
bars=int(input())

while count <= bars:
    b="█"* count
    print(f"Charging {b}")
    count += 1

count = 1
print("Please enter a phrase:")
phrase=input()

for item in phrase:
    count +=1
    print("Hi",end=" ")

print("Calculating the sum of the first 100 numbers...")
