print("Program Started!")
print("Please enter a standard character")
character = input()

ascii=ord(character)
print(f"The ASCII value of {character} is {ascii}")
print("Program Ended!")

print("Program Started!")
print("Please enter an ASCII code:")
code = int(input())
if code in range(32,127):
    ascii=chr(code)
    print(f"The character represented by the ASCII code {code} is {ascii}")
else:
    print("Please enter a value between 32 and 126")
print("Program Ended!")

