x = (input("Enter binary string: "))
n = int(input("Enter shift amount: "))
n %= len(x)
result = x[-n:] + x[:-n]
print("Shifted binary:", result)
