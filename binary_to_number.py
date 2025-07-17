b = input("Enter a binary number: ")
num = 0
for char in b:
    num = num * 2 + int(char)
print("Decimal:", num)
