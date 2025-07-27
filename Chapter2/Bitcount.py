x = input("Enter binary string: ")
num = int(x, 2) 

count = 0
while num:
    if num & 1:
        count += 1
    num >>= 1  

print("Number of 1's:", count)
