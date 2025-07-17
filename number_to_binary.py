a = int(input("Enter a number: "))
bits = []
while a != 0:
    bits.append(a % 2)
    a = a // 2

for bit in reversed(bits):
    print(bit)
