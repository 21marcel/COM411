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

